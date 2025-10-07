import asyncio
from foundry_local import FoundryLocalManager
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient


async def main():

    # Create a FoundryLocalManager instance. This will start the Foundry
    manager = FoundryLocalManager()
    modelInfo = manager.load_model("qwen2.5-0.5b")
    print(f"Model info: {modelInfo}")

    service_url = manager.service_uri
    service_url = service_url + "/v1"
    print(f"Foundry Local service URL: {service_url}")

    # check status of service
    manager.start_service()
    status = manager.is_service_running()
    print(f"Foundry Local service status: {status}")

    agent = ChatAgent(
    chat_client=OpenAIChatClient(
        model_id=modelInfo.id,
        base_url=service_url,
        api_key=manager.api_key  # API key is not required for local usage
        ),
    instructions="You are good at telling jokes.",
    name="Joker"
    )

    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

asyncio.run(main())