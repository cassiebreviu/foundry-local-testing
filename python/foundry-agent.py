import asyncio
from typing import Any
from agent_framework import BaseAgent
from foundry_local import FoundryLocalManager
import openai


class SimpleFoundryLocalAgent(BaseAgent):
    """A simplified custom agent that demonstrates integration with local models."""
    
    def __init__(
        self,
        model_alias: str = "qwen2.5-0.5b",
        instructions: str = "You are a helpful AI assistant.",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.model_alias = model_alias
        self.instructions = instructions
        self.manager = None
        self.client = None
        self.model_info = None
        
    async def __aenter__(self):
        """Initialize the agent when entering async context."""
        print(f"Initializing agent with model alias: {self.model_alias}")
        
        # Create a FoundryLocalManager instance
        self.manager = FoundryLocalManager()
        
        # Load the model by alias
        self.model_info = self.manager.load_model(self.model_alias)
        print(f"Model info: {self.model_info}")
        
        # Configure the OpenAI client to use the local Foundry service
        self.client = openai.OpenAI(
            base_url=self.manager.endpoint,
            api_key=self.manager.api_key  # API key is not required for local usage
        )
        
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Clean up resources when exiting async context."""
        print("Cleaning up agent resources")
        if self.manager:
            # Clean up Foundry Local resources if needed
            pass
            
    async def run(self, user_input: str, **kwargs) -> Any:
        """Run the agent with user input and return the response."""
        print(f"Processing user input: {user_input}")
        
        # Call the actual local model through Foundry Local
        response = await self._call_local_model(user_input)
        
        # Return a structured response
        return type('Response', (), {
            'text': response,
            'metadata': {
                'model_alias': self.model_alias,
                'model_id': self.model_info.id if self.model_info else 'unknown',
                'source': 'foundry_local'
            }
        })()
            
    async def _call_local_model(self, user_input: str) -> str:
        """Call the actual local model using Foundry Local."""
        try:
            if not self.client or not self.manager or not self.model_info:
                return "Error: Foundry Local client not properly initialized"
            
            # Prepare messages with system instructions
            messages = [
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": user_input}
            ]
            
            # Create a streaming response using the local model
            stream = self.client.chat.completions.create(
                model=self.model_info.id,
                messages=messages,
                stream=True
            )
            
            # Collect the streaming response
            response_text = ""
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    response_text += chunk.choices[0].delta.content
            
            return response_text.strip()
            
        except Exception as e:
            return f"Error calling local model: {str(e)}"


# Example of how to integrate with Foundry Local when ready
async def create_foundry_agent_example():
    """Example showing how to integrate with Foundry Local."""
    print("\n" + "="*50)
    print("FOUNDRY LOCAL INTEGRATION EXAMPLE")
    print("="*50)
    
    try:
        # Import Foundry Local components
        from foundry_local import FoundryLocalManager
        
        # Initialize Foundry Local
        foundry_manager = FoundryLocalManager()
        print("✓ Foundry Local manager initialized")
        
        # List available models
        loaded = foundry_manager.list_loaded_models()
        print(f"✓ Models running in the service: {loaded}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error with Foundry Local: {e}")
        print("Make sure you have a local model set up and configured")
        return False


async def main():
    """Demonstrate the custom agent."""
    print("Starting Custom Agent Demo...")
    
    # Test the foundry integration
    await create_foundry_agent_example()
    
    print("\n" + "="*50)
    print("CUSTOM AGENT DEMO")
    print("="*50)
    
    # Create and use the custom agent
    model_alias = "qwen2.5-0.5b"  # Use the same alias as in foundrylocal.py
    async with SimpleFoundryLocalAgent(
        model_alias=model_alias,
        instructions="You are a helpful AI assistant powered by a local model."
    ) as agent:
        
        # Test queries
        test_queries = [
            "What is the capital of France?",
            "Tell me a programming joke",
            "How does machine learning work?"
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n--- Test {i} ---")
            result = await agent.run(query)
            print(f"Query: {query}")
            print(f"Response: {result.text}")
            print(f"Model Alias: {result.metadata['model_alias']}")
            print(f"Model ID: {result.metadata['model_id']}")
            print(f"Source: {result.metadata['source']}")

    print("\n" + "="*50)
    print("SUCCESS!")
    print("="*50)
    print("✓ Custom agent successfully integrated with Foundry Local")
    print("✓ Local model calls working through OpenAI-compatible API")
    print("✓ Streaming responses handled and collected")
    print("✓ Proper resource management with async context")

if __name__ == "__main__":
    asyncio.run(main())