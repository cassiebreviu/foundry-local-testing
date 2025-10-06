import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from foundry_local import FoundryLocalManager

async def main():
    

    # By using an alias, the most suitable model will be downloaded
    # to your end-user's device.
    alias = "qwen2.5-0.5b"

    # Create a FoundryLocalManager instance. This will start the Foundry
    
    manager = FoundryLocalManager(alias)
    service_url = manager.service_uri
    print(f"Foundry Local service URL: {service_url}")
    # check status of service
    manager.start_service()
    status = manager.is_service_running()
    print(f"Foundry Local service status: {status}")
    # List available models
    loaded = manager.list_loaded_models()
    print(f"Models running in the service: {loaded}")
    # Set the model to use and generate a streaming response

    url = manager.endpoint + "/chat/completions"
    deployment_name = manager.get_model_info(alias).id
    print(f"Model info: {deployment_name}")
    # The Foundry Local endpoint uses HTTP by default.
    #update url to https
    url = url.replace("http://", "https://")
    print(f"Foundry Local endpoint: {url}")

    agent = AzureOpenAIChatClient(
        endpoint=url,
        deployment_name=deployment_name,
        api_key=manager.api_key  # API key is not required for local usage
    ).create_agent(
        instructions="You are good at telling jokes.",
        name="Joker"
    )

    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

asyncio.run(main())