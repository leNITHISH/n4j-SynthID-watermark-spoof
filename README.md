# Graph-Based LLM Watermark Attack using Neo4j

## Overview
This project demonstrates a black-box attack on LLM watermarking by extracting positional token biases and modeling them using a graph database (Neo4j).

## Tech Stack
- Python
- GPT-2 (Transformers)
- Neo4j

## Pipeline
1. Generate text using GPT-2
2. Build positional frequency map
3. Compute Z-scores
4. Store relationships in Neo4j
5. Query graph to extract dominant tokens

## How to Run

```bash
pip install -r requirements.txt
python main.py
