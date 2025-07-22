from unittest.mock import patch
from chat import get_conversation_chain
from tests.fake_llm import FakeLLM

@patch("chat.ChatOpenAI", new=FakeLLM)
def test_conversation_chain_mocked():
    chain = get_conversation_chain()
    result = chain.invoke(
        {"input": "Qual o presságio de um eclipse?"},
        config={"configurable": {"session_id": "sessao-teste"}}
    )
    assert result.content == "Resposta simulada"
