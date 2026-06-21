from fastapi import FastAPI
from Services import ClaudeService, ChatService
from anthropic import AnthropicFoundry
from Dtos import requestDto,responseDto

app = FastAPI()

client = ClaudeService.configureAISession()

items = []

@app.get("/")
def read_root():
    return {"Hello": "Thenul"}


@app.post("/items")
def read_item(q: str):
    items.append(q)
    return items

@app.post("/chat", response_model=responseDto.responseDto)
def chat(req: requestDto.requestDto):
    return ChatService.getAIResponse(req, client)

