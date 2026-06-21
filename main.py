# from anthropic import AnthropicFoundry
# from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from fastapi import FastAPI

# endpoint = "https://thenul-azureai-test1-resource.services.ai.azure.com/anthropic"
# deployment_name = "claude-opus-4-8"
# token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

# client = AnthropicFoundry(
#     azure_ad_token_provider=token_provider,
#     base_url=endpoint
# )
# prompt = input("Enter your prompt: ")
# message = client.messages.create(
#     model=deployment_name,
#     messages=[
#         {"role": "user", "content": prompt}
#     ],
#     max_tokens=1024,
# )

# print(message.content[0].text)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Thenul"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}