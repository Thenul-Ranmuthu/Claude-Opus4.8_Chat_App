import os
import openai
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

def configureAISession() -> openai.OpenAI:
    
    
    endpoint = os.getenv("ENDPOINT")#"https://thenul-azureai-test1-resource.services.ai.azure.com/anthropic"
    

    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )

    
    return project_client.get_openai_client()
    