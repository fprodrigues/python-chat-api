from fastapi import FastAPI
from schemas import Message
from chat import get_conversation_chain

app = FastAPI()
conversation = get_conversation_chain()

@app.post("/chat")
async def chat(msg: Message) -> dict:
    try:
        response = conversation.invoke(msg.message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
