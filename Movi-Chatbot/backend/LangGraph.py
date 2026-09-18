from typing import TypedDict, List, Dict

from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODELO_LLM
from rag import buscar_contexto


class EstadoMovi(TypedDict):
    pergunta: str
    historico: List[Dict[str, str]]
    documentos: List[Dict]
    contexto: str
    prompt: str
    resposta: str


def recuperar_contexto(state: EstadoMovi):
    documentos = buscar_contexto(state["pergunta"])

    partes = []

    for documento in documentos:
        partes.append(
            f"Fonte: {documento['arquivo']}\n"
            f"Categoria: {documento['categoria']}\n"
            f"Conteúdo:\n{documento['texto']}"
        )

    contexto = "\n\n---\n\n".join(partes)

    return {
        "documentos": documentos,
        "contexto": contexto
    }


def montar_prompt(state: EstadoMovi):
    historico = state.get("historico", [])

    texto_historico = ""

    for mensagem in historico[-6:]:
        papel = mensagem.get("role", "user")
        conteudo = mensagem.get("content", "")

        if papel == "user":
            texto_historico += f"Usuário: {conteudo}\n"
        else:
            texto_historico += f"Movi: {conteudo}\n"

    prompt = f"""
Você é o Movi, um assistente virtual educativo especializado em fisioterapia.

Sua função é responder perguntas utilizando principalmente as informações
presentes no CONTEXTO recuperado da base de conhecimento.

REGRAS:

- Responda em português do Brasil.
- Seja claro e educativo.
- Não invente informações.
- Não faça diagnósticos.
- Não prescreva tratamentos individualizados.
- Não substitua a avaliação de um fisioterapeuta.
- Caso o contexto não possua informação suficiente, informe isso claramente.
- Em situações de emergência ou sintomas graves, recomende procurar atendimento profissional.

HISTÓRICO DA CONVERSA:

{texto_historico}

CONTEXTO RECUPERADO:

{state["contexto"]}

PERGUNTA:

{state["pergunta"]}

Responda utilizando o contexto apresentado.
"""

    return {"prompt": prompt}


def gerar_resposta(state: EstadoMovi):
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY não encontrada. Configure a chave no arquivo .env."
        )

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODELO_LLM,
        temperature=0.2
    )

    resposta = llm.invoke(state["prompt"])

    return {"resposta": resposta.content}


def criar_grafo():
    grafo = StateGraph(EstadoMovi)

    grafo.add_node("recuperar_contexto", recuperar_contexto)
    grafo.add_node("montar_prompt", montar_prompt)
    grafo.add_node("gerar_resposta", gerar_resposta)

    grafo.add_edge(START, "recuperar_contexto")
    grafo.add_edge("recuperar_contexto", "montar_prompt")
    grafo.add_edge("montar_prompt", "gerar_resposta")
    grafo.add_edge("gerar_resposta", END)

    return grafo.compile()


grafo_movi = criar_grafo()


def perguntar_movi(pergunta, historico=None):
    resultado = grafo_movi.invoke({
        "pergunta": pergunta,
        "historico": historico or [],
        "documentos": [],
        "contexto": "",
        "prompt": "",
        "resposta": ""
    })

    return {
        "resposta": resultado["resposta"],
        "fontes": resultado["documentos"]
    }