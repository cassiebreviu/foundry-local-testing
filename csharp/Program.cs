using System;
using System.Threading.Tasks;
using Microsoft.AI.Foundry.Local;
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OpenAI;

class Program
{
    static async Task Main(string[] args)
    {
        // Create Foundry Local manager
        var manager = new FoundryLocalManager();

        // Load the model
        var modelInfo = await manager.LoadModelAsync("qwen2.5-0.5b");

        Console.WriteLine($"Loaded model: {modelInfo.ModelId}");
        Console.WriteLine($"Model details: {manager.Endpoint}");

        // Create OpenAI client pointing to Foundry Local endpoint
        var openAIClient = new OpenAI.OpenAIClient(
            new System.ClientModel.ApiKeyCredential(manager.ApiKey),
            new OpenAI.OpenAIClientOptions { Endpoint = manager.Endpoint }
        );
        
        // Get chat client and convert to IChatClient
        var chatClient = openAIClient.GetChatClient(modelInfo.ModelId).AsIChatClient();
        
        // Create AI agent from the chat client
        var agent = new ChatClientAgent(
            chatClient,
            instructions: "You are good at telling jokes.",
            name: "Joker");
        
        // Run the agent
        var response = await agent.RunAsync("Tell me a joke about a pirate.");
        Console.WriteLine(response);
    }
}