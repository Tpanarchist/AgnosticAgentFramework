# OpenAI API Quickstart Reference Sheet

## Authentication Essentials
```yaml
API_KEY:
  storage_locations:
    - Environment variables
    - .env files
    - Configuration files
  environment_variables:
    name: "OPENAI_API_KEY"
    format: "sk-********************************"

setup_commands:
  macos_linux: 'export OPENAI_API_KEY="your_api_key_here"'
  windows: 'setx OPENAI_API_KEY "your_api_key_here"'
```

## SDK Installation
```yaml
python:
  package: openai
  install_command: "pip install openai"
  import_statement: "from openai import OpenAI"
  client_initialization: "client = OpenAI()"
```

## Basic Request Structure
```python
request_template = {
    "client": "OpenAI instance",
    "endpoint": "chat.completions",
    "required_params": {
        "model": "string",  # e.g., "gpt-4", "gpt-3.5-turbo"
        "messages": [
            {
                "role": "system | user | assistant",
                "content": "string"
            }
        ]
    }
}
```

## Core Components for Framework Implementation

### 1. Client Setup
```python
class APIClientSetup:
    required_env_vars = ["OPENAI_API_KEY"]
    client_config = {
        "api_key": "env.OPENAI_API_KEY",
        "organization": "optional",
        "base_url": "optional"
    }
```

### 2. Basic Message Structure
```python
message_template = {
    "system_message": {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    "user_message": {
        "role": "user",
        "content": "actual_prompt_here"
    }
}
```

### 3. Response Format
```python
response_structure = {
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "string"
            },
            "finish_reason": "stop|length|content_filter",
            "index": 0
        }
    ],
    "created": "timestamp",
    "model": "model_name",
    "usage": {
        "prompt_tokens": "int",
        "completion_tokens": "int",
        "total_tokens": "int"
    }
}
```

## Framework Implementation Considerations

### 1. Authentication Handler
```python
class AuthHandler:
    responsibilities = [
        "API key validation",
        "Environment variable management",
        "Key rotation support",
        "Error handling for auth issues"
    ]
```

### 2. Client Factory
```python
class ClientFactory:
    features = [
        "Client instance creation",
        "Configuration management",
        "Error handling",
        "Retry logic"
    ]
```

### 3. Request Builder
```python
class RequestBuilder:
    components = [
        "Message formatting",
        "Parameter validation",
        "Model selection",
        "Request optimization"
    ]
```

## Error Handling Patterns
```yaml
common_errors:
  - InvalidAPIKey: "Authentication failed"
  - RateLimitExceeded: "Too many requests"
  - InvalidRequestError: "Malformed request"
  - ServiceUnavailable: "API service issues"

error_handling_strategy:
  retry_patterns:
    - rate_limits: "Exponential backoff"
    - network_errors: "Linear retry"
    - service_unavailable: "Circuit breaker"
```

## Best Practices
```yaml
security:
  - Never hardcode API keys
  - Use environment variables
  - Implement key rotation
  - Validate API key format

performance:
  - Implement request caching
  - Use connection pooling
  - Monitor rate limits
  - Implement retry mechanisms

reliability:
  - Handle network timeouts
  - Implement circuit breakers
  - Log all API interactions
  - Monitor response times
```
