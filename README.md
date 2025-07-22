# 🏰 Python Chat API Medieval

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![CI](https://github.com/fprodrigues/python-chat-api/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/fprodrigues/python-chat-api)
![Made with LangChain](https://img.shields.io/badge/made%20with-LangChain-purple)

Uma API de chat feita com FastAPI e LangChain que simula um **camponês medieval** supersticioso, simplório e engraçado. O modelo responde como se estivesse no século XIV, usando crenças populares e humor típico da Idade Média. A aplicação usa a OpenAI (GPT-3.5-Turbo) com um prompt customizado em **português**.

---

## 📋 Sumário (Summary)

- [Descrição](#descrição)
- [Tecnologias](#tecnologias)
- [Como executar](#como-executar)
- [Testes](#testes)
- [Exemplo de uso](#exemplo-de-uso)
- [English version](#english-version)

---

## 📜 Descrição

Este projeto oferece uma interface HTTP simples com a biblioteca FastAPI, que expõe um endpoint de chat (`/chat`). Ele utiliza a `LangChain`, com `ChatOpenAI`, `PromptTemplate` e `ConversationChain` para manter o histórico das conversas.

O prompt está em **português**, e força o modelo a responder como um camponês medieval supersticioso e um tanto cômico, mantendo as respostas curtas e pitorescas.

---

## ⚙️ Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- LangChain
- OpenAI API
- pytest
- dotenv

---

## ▶️ Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/python-chat-api.git
cd python-chat-api
```

2. **Crie o .env**

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Executar a aplicação:**

```bash
uvicorn main:app --reload
```

4. **Acessar as docs:**

```bash
http://localhost:8000/docs
```

## 🧪 Testes

**Execute com:**

```bash
pytest
```
Mock de LLM incluso para não usar tokens da OpenAI nos testes.

## 💬 Exemplo de uso

```bash
POST /chat
{
  "message": "Qual o presságio de um eclipse?"
}
```
Resposta esperada
```bash
{
  "response": "Eclipse? Vixe... é sinal de dragão faminto!"
}
```