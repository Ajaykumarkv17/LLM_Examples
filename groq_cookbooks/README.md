# Groq Cookbooks

A collection of examples demonstrating various capabilities of Groq's LLM APIs across different use cases.

## Contents

### 1. Parallel Tool Use
Located in `/Parallel_tool_use`
- `parallel_tool.ipynb`: Demonstrates concurrent execution of LLM tasks
- Shows how to effectively parallelize multiple LLM operations
- Includes performance optimization techniques

### 2. Structured Output
Located in `/Structured_output`
- `Instructor_st_output.ipynb`: Examples of generating structured outputs
- Shows how to use Instructor framework with Groq
- Demonstrates type-safe output generation

### 3. Text to SQL
Located in `/Text2sql`
- `function_calling_sql.ipynb`: Implementation of natural language to SQL conversion
- Working with sample datasets:
  - employees.csv
  - purchases.csv
- Verified SQL queries examples in `/verified-queries`:
  - Employees without purchases
  - Most expensive purchases
  - Most recent purchases
  - Tesla-related queries

## Getting Started

1. Install required dependencies:
```bash
pip install groq instructor pandas jupyter
```

2. Set up your Groq API key:
```bash
export GROQ_API_KEY=your_key_here
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

## Key Features
- Parallel processing capabilities
- Structured data handling
- SQL query generation
- Type-safe output generation
- Verified query examples

## Prerequisites
- Python 3.8+
- Groq API key
- Basic understanding of:
  - SQL
  - Pandas
  - Jupyter notebooks

## Additional Resources
- [Groq Documentation](https://docs.groq.com)
- [Instructor Framework](https://github.com/jxnl/instructor)
