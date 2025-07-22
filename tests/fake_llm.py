from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from typing import List, Any

class FakeLLM(BaseChatModel):
    @property
    def _llm_type(self) -> str:
        return "fake-llm"

    def _generate(self, messages: List[Any], stop: Any = None, **kwargs) -> ChatResult:
        message = AIMessage(content="Resposta simulada")
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])
