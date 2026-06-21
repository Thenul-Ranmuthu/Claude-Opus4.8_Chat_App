import os
from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

def configureAISession() -> AnthropicFoundry:
    
    load_dotenv()
    
    endpoint = os.getenv("ENDPOINT")#"https://thenul-azureai-test1-resource.services.ai.azure.com/anthropic"
    token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

    client = AnthropicFoundry(
        azure_ad_token_provider=token_provider,
        base_url=endpoint
    )
    return client
    
    