# FastAPI Learning

A simple repository for me to learn FastAPI - a fast web framework for building APIs with Python.

## About

This project contains basic FastAPI examples and experiments as I learn the framework. FastAPI is known for being:
- Easy to learn
- Fast development
- High performance

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

Start the development server:
```bash
uvicorn main:app --reload
```

## Current Features

- Basic "Hello World" endpoint at `/` (see [main.py](main.py))
- Development notes and learning progress tracked in [log.org](log.org)

## Learning Goals

- Understanding FastAPI basics
- Working with routes and HTTP methods
- Building a simple API application
- Exploring FastAPI's automatic documentation features

## Notes

This is a learning project, so the code will evolve as I explore different FastAPI concepts and patterns.