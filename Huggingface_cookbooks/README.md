# Hugging Face Cookbooks

A comprehensive collection of examples demonstrating various capabilities of Hugging Face's ecosystem, from LLM inference to RAG implementations and agent-based systems.

## Contents

### 1. Core Examples
- `Agentic_text2sql.ipynb`: Text-to-SQL implementation with agent-based approach
- `KV_Cache_nvidia.ipynb`: NVIDIA optimization using KV caching
- `meta_llama_3.2.py` & `meta_llama_3.2_text.py`: LLaMA model implementations
- `structured_highlighting_rag.ipynb`: RAG with structured text highlighting

### 2. Agents
Located in `/Agents`
- `Data_analyst_agent.ipynb`: Implementation of data analysis agent
- Visualization examples in `/figures`:
  - Age distribution analysis
  - SibSp distribution plots
  - Survival rate analysis by class

### 3. Hugging Face LLM Inference
Located in `/Huggingface_llm_inference`
- `agentic_rag.ipynb`: Agent-enhanced RAG implementation
- `RAG_backed_by_SQL_and_Jina_Reranker.ipynb`: SQL-backed RAG with reranking
- `smol_agents.ipynb`: Lightweight agent implementations
- Includes sample database: `videogames.db`

### 4. RAG (Retrieval Augmented Generation)
Located in `/RAG`
- `Rag_with_milvus.ipynb`: Vector store implementation with Milvus
- `rag_with_unstructured_io.ipynb`: Unstructured data handling
- Example documents:
  - The-AI-Act.pdf
  - Prompt engineering guide
- FAISS index implementations

### 5. VLM Small Agents
Located in `/vlm_smol_agents`
- `smol_vlm_agents.ipynb`: Vision Language Model implementations with lightweight agents

## Getting Started

1. Install required dependencies:
```bash
pip install transformers torch pandas numpy faiss-cpu unstructured
```

2. Set up your Hugging Face API key:
```bash
export HUGGINGFACE_API_KEY=your_key_here
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

## Key Features
- LLM model inference and optimization
- RAG implementations with various backends
- Agent-based systems
- Vision-language model integration
- Data analysis and visualization
- Vector store implementations

## Prerequisites
- Python 3.8+
- Hugging Face API key
- CUDA-compatible GPU (recommended for some examples)
- Basic understanding of:
  - PyTorch
  - Transformers
  - Vector databases
  - Jupyter notebooks

## Additional Resources
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
