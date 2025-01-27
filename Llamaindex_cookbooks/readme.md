# LlamaIndex Cookbooks

A collection of examples showcasing LlamaIndex capabilities for document processing, retrieval-augmented generation (RAG), and agent-based workflows.

## Contents

### 1. Core Examples
- `gpt4o_mini.ipynb`: Implementation using GPT-4 optimized mini models
- `llama_parse_eg.py`: Document parsing examples using LlamaParse
- JSON document examples:
  - `docs.jsonl`
  - `docs_gpt4o-mini.jsonl`

### 2. Multimodal RAG Examples
- `multimodal_rag_slide_deck.ipynb`: RAG implementation for slide decks
- `Multimodal_rag.ipynb`: General multimodal RAG implementation
- Sample data in `/data` directory including report.pdf

### 3. Agent Workflows
Located in `/agentworkflows`
- `agent.ipynb`: Implementation of agent-based workflows
- Examples of:
  - Task decomposition
  - Agent coordination
  - Workflow automation

## Getting Started

1. Install required dependencies:
```bash
pip install llama-index pypdf transformers pillow jupyter
```

2. Set up your API keys:
```bash
export OPENAI_API_KEY=your_openai_key  # or other LLM provider
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

## Key Features
- Document processing and parsing
- Multimodal RAG implementations
- Agent-based workflows
- PDF and slide deck handling
- JSON document processing
- Integration with various LLM providers

## Prerequisites
- Python 3.8+
- OpenAI API key or other LLM provider credentials
- Basic understanding of:
  - RAG concepts
  - Document processing
  - Jupyter notebooks
  - Vector embeddings

## Additional Resources
- [LlamaIndex Documentation](https://docs.llamaindex.ai)
- [LlamaParse Documentation](https://docs.llamaindex.ai/en/stable/module_guides/parsing/llamaparse.html)
- [LlamaIndex GitHub Repository](https://github.com/run-llama/llama_index)
