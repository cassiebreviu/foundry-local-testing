# Local AI Development Workshop

A hands-on workshop for building AI agents with local models using Foundry Local and the Microsoft Agent Framework.

## Workshop Overview

This workshop teaches you how to build, deploy, and evaluate AI agents using local language models. You'll learn to work with Foundry Local for running models on your own hardware, the Microsoft Agent Framework (AGF) for building intelligent agents, and best practices for evaluation.

---

## Part 1: Getting Started with LLMs

### 📚 Lecture: Introduction to Large Language Models
- What are LLMs and how do they work?
- Local vs. cloud-hosted models
- Introduction to Foundry Local
- Model selection and capabilities

### 🛠️ Practical: Setting Up Foundry Local

**Objectives:**
- Install and configure Foundry Local
- Download and run your first local model
- Interact with models via command line

**Steps:**

1. **Install Foundry Local**
   ```bash
   # Follow installation instructions for your OS
   # https://github.com/microsoft/foundry-local
   ```

2. **Load a model**
   ```bash
   # Start Foundry Local service
   foundry-local start
   
   # Load a small model to get started
   foundry-local load qwen2.5-0.5b
   ```

3. **Test in command line**
   ```bash
   # Interact with the model
   foundry-local chat qwen2.5-0.5b
   ```

4. **Try the Python example**
   ```bash
   cd python
   pip install -r requirements.txt
   python foundrylocal.py
   ```

5. **Try the C# example**
   ```bash
   cd csharp
   dotnet build
   dotnet run
   ```

**Key Concepts:**
- Model aliases and versioning
- API endpoints and compatibility
- Streaming vs. non-streaming responses

---

## Part 2: Working with Agent Framework (AGF)

### 📚 Lecture: Introduction to Microsoft Agent Framework
- What is an agent?
- Agent Framework architecture
- Types of agents (ChatAgent, CustomAgent)
- Agent instructions and behaviors

### 🛠️ Practical: Single Agent Samples

**Objectives:**
- Create your first AI agent
- Understand agent instructions
- Work with different agent types

**Examples:**

1. **Simple Chat Agent** (Python)
   ```bash
   cd python
   python foundry-local-with-agf.py
   ```
   
   Review the code to understand:
   - Creating a ChatAgent
   - Connecting to Foundry Local endpoint
   - Setting instructions
   - Running queries

2. **Custom Agent** (C#)
   ```bash
   cd csharp
   dotnet run
   ```
   
   Explore:
   - Custom agent implementation
   - Structured responses
   - Metadata tracking
   - Streaming support

3. **Experiment with Instructions**
   - Modify agent instructions to change behavior
   - Try different personas (helpful assistant, code reviewer, creative writer)
   - Test how instructions affect responses

**Key Concepts:**
- Agent initialization and setup
- System instructions vs. user prompts
- Agent state management
- Response handling

---

## Part 3: Working with AGF Workflows

### 📚 Lecture: Multi-Agent Workflows
- What are workflows?
- Agent collaboration patterns
- Sequential vs. parallel execution
- State management across agents

### 🛠️ Practical: Creative Writer Workflow

**Objectives:**
- Build a multi-agent workflow
- Understand agent handoffs
- Manage workflow state

**Key Concepts:**
- Agent specialization
- Workflow orchestration
- Context passing

---

## Part 4: Understanding How to Evaluate

### 📚 Lecture: LLM Evaluation Fundamentals
- Why evaluation matters
- Types of evaluations
- Common evaluation metrics
- Evaluation frameworks and tools

### 🛠️ Practical: Performing Evaluations

**Objectives:**
- Design evaluation datasets
- Implement automated evaluations
- Analyze results and iterate


---

## Prerequisites

### Software Requirements
- **Python 3.9+** or **.NET 9.0+**
- **Foundry Local** installed and running
- **Git** for cloning the repository

### Knowledge Prerequisites
- Basic programming in Python or C#
- Understanding of async/await patterns
- Familiarity with APIs (helpful but not required)

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd foundry-local-testing
   ```

2. **Choose your language track**
   
   **Python:**
   ```bash
   cd python
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   
   **C#:**
   ```bash
   cd csharp
   dotnet restore
   dotnet build
   ```

3. **Install Foundry Local**
   - Follow the official Foundry Local installation guide
   - Start the service
   - Load at least one model (e.g., `qwen2.5-0.5b`)

4. **Verify setup**
   ```bash
   # Test that Foundry Local is running
   curl http://localhost:5272/v1/models
   ```

---

### Going Further
- Experiment with different models
- Build domain-specific agents
- Create multi-step workflows
- Implement advanced evaluation metrics
- Add observability and logging
- Deploy agents to production

---

## Resources

### Documentation
- [Foundry Local Documentation](https://github.com/microsoft/foundry-local)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

### Additional Learning
- LLM evaluation frameworks (LangChain, PromptFlow)
- Agent design patterns
- Prompt engineering techniques
- Production deployment strategies

---

## Support

For questions or issues:
1. Check the documentation in each language folder
2. Review example code and comments
3. Consult official Microsoft Agent Framework docs
4. Open an issue in the repository

---

## License

This workshop material is provided for educational purposes.

---

## Next Steps

After completing this workshop, you should be able to:
- ✅ Set up and run local LLMs with Foundry Local
- ✅ Build single-agent applications with AGF
- ✅ Create multi-agent workflows
- ✅ Evaluate and improve agent performance
- ✅ Deploy local AI agents in production

**Happy building! 🚀**
