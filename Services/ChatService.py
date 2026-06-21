import os
from Dtos.responseDto import responseDto
from Dtos.requestDto import requestDto
from anthropic import AnthropicFoundry
from dotenv import load_dotenv

load_dotenv()
deployment_name = os.getenv("DEPLOYMENT_NAME")

def getAIResponse(req: requestDto, client: AnthropicFoundry) -> responseDto:
    
    message = client.messages.create(
        model=deployment_name,
        messages=[
            {"role": "user", "content": req.prompt}
        ],
        max_tokens=1024,
    )

    return responseDto(response=message.content[0].text)