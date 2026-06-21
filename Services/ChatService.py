import os
from Dtos import responseDto,requestDto
from anthropic import AnthropicFoundry
from dotenv import load_dotenv

load_dotenv()
deployment_name = os.getenv("DEPLOYMENT_NAME")

def getAIResponse(prompt: requestDto, client: AnthropicFoundry) -> responseDto:
    
    message = client.messages.create(
        model=deployment_name,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
    )

    return responseDto(response=message.content[0].text)