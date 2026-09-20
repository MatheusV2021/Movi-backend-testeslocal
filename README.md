# 🦫 Movi — Fisioterapeuta Virtual

O **Movi** é um chatbot educativo voltado para a área de **Fisioterapia**, desenvolvido para responder perguntas em linguagem natural utilizando uma base de conhecimento especializada.

O projeto utiliza **RAG (Retrieval-Augmented Generation)** para buscar informações relevantes nos documentos da base antes de gerar uma resposta, tornando as respostas mais contextualizadas e relacionadas ao conteúdo fornecido.

> ⚠️ **Importante:** O Movi possui finalidade educativa e informativa. Ele não substitui a avaliação, o diagnóstico ou o acompanhamento de um fisioterapeuta ou outro profissional de saúde.

---

## 🎯 Objetivo

O objetivo do projeto é desenvolver uma aplicação web capaz de:

* Receber perguntas sobre Fisioterapia;
* Consultar uma base de conhecimento formada por documentos;
* Encontrar os trechos mais relevantes para a pergunta;
* Utilizar esses trechos como contexto para uma LLM;
* Gerar uma resposta através de um fluxo RAG;
* Disponibilizar tudo por meio de uma interface simples de chatbot.

---

## 🧠 Como funciona

O funcionamento do Movi segue basicamente este fluxo:

**Usuário → Pergunta → RAG → Busca na base vetorial → Contexto → LLM → Resposta**

Os documentos da base de conhecimento são processados e divididos em pequenos trechos (**chunks**).

Esses trechos são transformados em **embeddings**, representações numéricas que permitem comparar semanticamente a pergunta do usuário com o conteúdo disponível.

A busca vetorial encontra os conteúdos mais relacionados à pergunta e envia esse contexto para a LLM responsável pela geração da resposta.

O fluxo é organizado utilizando **LangGraph**.

---

## 🛠️ Tecnologias utilizadas

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* LangChain
* LangGraph
* FAISS
* Sentence Transformers

### Inteligência Artificial

* RAG (Retrieval-Augmented Generation)
* Embeddings
* Busca por similaridade
* LLM para geração das respostas

---

## 📚 Base de conhecimento

A base de conhecimento do Movi é composta por materiais relacionados à **Fisioterapia**.

Os documentos são processados pelo backend e utilizados para criar uma base vetorial.

Fluxo de processamento:

```text
PDF
 ↓
Extração do texto
 ↓
Divisão em chunks
 ↓
Geração de embeddings
 ↓
Indexação no FAISS
 ↓
Base vetorial
```

Quando uma pergunta é realizada, o sistema procura nessa base os trechos semanticamente mais próximos.

---

## 📂 Estrutura do projeto

```text
Movi-Chatbot/
│
├── frontend/
│   ├── assets/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   │
│   └── index.html
│
├── backend/
│   ├── base_conhecimento/
│   ├── base_vetorial/
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

*A estrutura pode sofrer alterações conforme a evolução do projeto.*

---

## 🚀 Executando o projeto

### 1. Clone o repositório

```bash
git clone <URL-DO-REPOSITORIO>
```

Entre na pasta:

```bash
cd Movi-Chatbot
```

### 2. Crie o ambiente virtual

Dentro da pasta do backend:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Adicione a base de conhecimento

Coloque os documentos utilizados pelo Movi na pasta destinada à base de conhecimento.

Depois, execute o processo de criação/indexação da base vetorial antes de iniciar o chatbot.

### 5. Inicie o backend

```bash
uvicorn main:app --reload
```

Por padrão, a API ficará disponível localmente na porta configurada pelo projeto.

### 6. Abra o frontend

Abra o arquivo:

```text
frontend/index.html
```

Também é possível utilizar uma extensão como **Live Server** para executar o frontend localmente.

---

## 💬 Exemplo de funcionamento

```text
Usuário:
O que é fisioterapia aquática?

Movi:
A fisioterapia aquática é uma abordagem terapêutica que utiliza
exercícios realizados em ambiente aquático como parte do processo
de reabilitação...
```

A resposta é produzida utilizando informações recuperadas da base de conhecimento do projeto.

---

## 🔎 RAG

O **RAG (Retrieval-Augmented Generation)** permite combinar recuperação de informações com modelos de linguagem.

No Movi, o processo acontece em três etapas principais:

1. **Recuperação:** busca conteúdos relacionados à pergunta na base vetorial.
2. **Contextualização:** os trechos encontrados são utilizados como contexto.
3. **Geração:** a LLM recebe a pergunta e o contexto para produzir a resposta.

Isso permite que o chatbot utilize uma base específica de Fisioterapia em vez de depender somente do conhecimento geral da LLM.

---

## 🦫 Sobre o Movi

O Movi foi pensado para possuir uma identidade simples e amigável.

A **capivara de jaleco** é utilizada como mascote da plataforma, representando o fisioterapeuta virtual durante a interação com o usuário.

A proposta é tornar o acesso ao conteúdo de Fisioterapia mais simples, didático e interativo.

---

## 👥 Equipe

Projeto desenvolvido por:

* **Matheus Vinnycius Vasconcelos de Santana**
* **Pedro Henrique Jerônimo da Silva**
* **Ludmylla Dias de Souza Santos**

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como atividade acadêmica envolvendo:

* Desenvolvimento Web;
* Python;
* Inteligência Artificial;
* RAG;
* LangGraph;
* LLMs;
* Busca por similaridade;
* Bancos vetoriais.

---

## ⚠️ Aviso

As informações fornecidas pelo **Movi** possuem caráter exclusivamente **educativo e informativo**.

O sistema não realiza diagnóstico médico e não deve ser utilizado como substituto para atendimento, avaliação ou tratamento realizado por profissionais qualificados.
