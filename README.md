# Local AI Development Workshop

A hands-on workshop for building AI agents with local models using Foundry Local and the Microsoft Agent Framework.

## Workshop Overview

This workshop teaches you how to build, deploy, and evaluate AI agents using local language models. You'll learn to work with Foundry Local for running models on your own hardware, the Microsoft Agent Framework (AGF) for building intelligent agents, and best practices for evaluation.

### Prerequisites

- **Python 3.9+** or **.NET 9.0+**
- **Git** for cloning the repository
- Basic programming in Python or C#
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

**Get Started with Foundry Local CLI:**
- Follow the instructions to [get started with Foundry Local CLI](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started)


**Key Concepts:**
- Understanding how to run Foundry Models locally
- Try out different models and understand the differences

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


## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd foundry-local-workshop
   ```

2. **Choose your language track**
   
   **Python:**
   ```bash
   cd python
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python foundry-local-with-agf.py
   ```
   
   **C#:**
   ```bash
   cd csharp
   dotnet restore
   dotnet build
   dotnet run
   ```

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

**Happy building! 🚀**
