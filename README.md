# Uncensored AI Python Package

A lightweight Python client for the Uncensored AI API

## Features

- Chat completions - with streaming support
- Fine-tuning 
- Model listing 
- Image generation
- CLI for easy account management
- Both global and client-based usage patterns

## Installation

```bash
pip install uncensored
```

## Usage

```python
import uncensored

# Global usage
uncensored.api_key = "YOUR-KEY-HERE"

response = uncensored.ChatCompletion.create(
    model="model-t",
    messages=[{"role": "user", "content": "Say wasa"}],
    stream=True,
)

for chunk in response:
    print(chunk)

# OR using an optional client-like usage
client = uncensored.Client(api_key="YOUR-KEY-HERE")
models = client.list_models()
print(models)
```

## CLI

```bash
# Log in (fetch/store API key)
uncensored login

# Check your usage/balance
uncensored balance

# List available models
uncensored list-models
```

contact: devs@uncensored.com 

by uncensored.com
