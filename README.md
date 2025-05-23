# Anyshift-AI-Screener
# AnyShift AI-Powered Candidate Screening System

## Overview
This repository contains a prototype AI-powered candidate screening assistant designed for AnyShift, a startup revolutionizing shift-based hiring.

The system:
- Parses candidate free-text responses into structured data using OpenAI GPT via LangChain
- Scores candidate fit to shift posting requirements with detailed sub-scores and explanations
- Returns recruiter-friendly outputs with explainability
- Limits LLM calls to 2 per screening for cost and speed efficiency
- Includes a FastAPI demo API and containerized deployment with Docker

## Repo Structure
- `screen_candidate.py`: Main screening logic with LangChain prompt chains
- `app.py`: FastAPI app exposing `/screen` endpoint for API demo
- `prompts/`: Prompt templates for extraction and scoring
- `utils.py`: Helper functions for scoring and parsing
- `data/input.json`: Sample candidate + shift JSON input
- `Dockerfile`: Containerize the FastAPI screening API
- `requirements.txt`: Python dependencies

## How to Use

1. Set your OpenAI API key in the environment variable `OPENAI_API_KEY`
2. Run screening script on sample data:

```bash
python screen_candidate.py data/input.json