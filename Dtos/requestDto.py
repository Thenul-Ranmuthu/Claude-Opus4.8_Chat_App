from pydantic import BaseModel

class requestDto(BaseModel):
    prompt: str