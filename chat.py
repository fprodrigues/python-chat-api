from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from config import OPENAI_API_KEY
from prompts.medieval import medieval_prompt

def get_conversation_chain():
    prompt = PromptTemplate.from_template(medieval_prompt)

    llm = ChatOpenAI(
        temperature=0.8,
        model_name="gpt-3.5-turbo",
        openai_api_key=OPENAI_API_KEY,
    )

    # Este é o core do chain
    def invoke_chain(inputs):
        formatted = prompt.format(**inputs)
        return llm.invoke(formatted)

    chain = RunnableLambda(invoke_chain)

    # Sessão de memória — retornada por sessão_id
    def get_session_history(session_id: str):
        return InMemoryChatMessageHistory()

    return RunnableWithMessageHistory(
        chain,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
