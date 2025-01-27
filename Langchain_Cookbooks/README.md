# LangChain Cookbooks

Examples demonstrating LangChain's capabilities for building applications with large language models, focusing on database integration and advanced LLM usage.

## Contents

### 1. Databricks SQL Integration (databricks_sql_db.ipynb)
- Integration with Databricks SQL
- Demonstrates database querying and manipulation
- Examples of combining LLMs with SQL operations

### 2. Smart LLM Usage (smart_llm.ipynb)
- Advanced LLM integration techniques
- Showcases intelligent prompt engineering
- Examples of chain and agent implementations

## Getting Started

1. Install required dependencies:
```bash
pip install langchain databricks-sql-connector jupyter
```

2. Configure necessary environment variables:
```bash
export DATABRICKS_HOST=your_databricks_host
export DATABRICKS_TOKEN=your_token
export OPENAI_API_KEY=your_openai_key  # or other LLM provider
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

## Key Features
- SQL database integration
- Intelligent LLM interactions
- Chain and agent implementations
- Databricks connectivity
- Smart prompt engineering

## Prerequisites
- Python 3.8+
- Databricks workspace access
- OpenAI API key or other LLM provider credentials
- Basic understanding of:
  - SQL
  - LangChain concepts
  - Jupyter notebooks

## Additional Resources
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Databricks SQL Documentation](https://docs.databricks.com/sql/index.html)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
