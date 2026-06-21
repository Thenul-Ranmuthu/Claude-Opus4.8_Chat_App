import os
import openai
from Dtos.responseDto import responseDto
from Dtos.requestDto import requestDto
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
agent = os.getenv("MY_AGENT")
version = os.getenv("MY_VERSION")

def getAIResponse(req: requestDto, client: openai.OpenAI) -> responseDto:
    

    response = client.responses.create(
        input=[{"role": "user", "content": req.prompt}],
        extra_body={"agent_reference": {"name": agent, "version": version, "type": "agent_reference"}},
    )

    return responseDto(response=response.output_text)