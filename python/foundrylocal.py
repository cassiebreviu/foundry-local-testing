
from foundry_local import FoundryLocalManager
import openai

# By using an alias, the most suitable model will be selected
# to your end-user's device.
alias = "qwen2.5-0.5b"

# Create a FoundryLocalManager instance. This will start the Foundry.
manager = FoundryLocalManager()

# Load a model by alias
model_info = manager.load_model(alias)
print(f"Model info: {model_info}")

# List loaded models
loaded = manager.list_loaded_models()
print(f"Models running in the service: {loaded}")

# Configure the client to use the local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key  # API key is not required for local usage
)

# Set the model to use and generate a streaming response
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is the golden ratio?"}],
    stream=True
)

# Print the streaming response
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)