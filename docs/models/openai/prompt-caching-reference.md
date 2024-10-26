# OpenAI Prompt Caching Guide

## Model Support
```yaml
supported_models:
  base_models:
    - "gpt-4o"
    exclusions:
      - "gpt-4o-2024-05-13"
      - "chatgpt-4o-latest"
    features: ["Full caching support"]
  
  additional_models:
    - "gpt-4o-mini"
    - "o1-preview"
    - "o1-mini"

caching_requirements:
  minimum_tokens: 1024
  cache_increments: 128
  sequence: [1024, 1152, 1280, 1408, "..."]
```

## Cache Mechanics
```yaml
cache_process:
  lookup:
    description: "Check if prompt prefix exists in cache"
    trigger: "Every API request"
  
  hit:
    action: "Use cached result"
    benefits:
      latency: "Up to 80% reduction"
      cost: "50% reduction for long prompts"
  
  miss:
    action: "Process full prompt"
    followup: "Cache prefix for future requests"

cache_retention:
  normal_period: "5-10 minutes of inactivity"
  off_peak_period: "Up to one hour"
  eviction: "Automatic based on inactivity"
```

## Cacheable Components
```yaml
cacheable_elements:
  messages:
    - "System messages"
    - "User messages"
    - "Assistant messages"
  
  images:
    format:
      - "URL links"
      - "Base64 encoded data"
    requirements: "Identical detail parameter"
  
  tools:
    components:
      - "Messages array"
      - "Available tools list"
    minimum_requirement: "1024 tokens combined"
  
  structured_outputs:
    location: "Prefix to system message"
    type: "Schema definition"
```

## Best Practices
```yaml
prompt_structure:
  prefix:
    content: "Static/repeated content"
    placement: "Beginning of prompt"
    examples:
      - "System instructions"
      - "Common prompts"
      - "Standard examples"
  
  suffix:
    content: "Dynamic/variable content"
    placement: "End of prompt"
    examples:
      - "User-specific data"
      - "Request-specific parameters"
      - "Dynamic inputs"

optimization_strategies:
  metrics_monitoring:
    - "Cache hit rates"
    - "Latency reduction"
    - "Cached token percentage"
  
  cache_efficiency:
    - "Use longer prompts (>1024 tokens)"
    - "Schedule during off-peak hours"
    - "Maintain consistent request patterns"
```

## Performance Monitoring
```yaml
usage_tracking:
  response_object:
    format: |
      {
        "usage": {
          "prompt_tokens": int,
          "completion_tokens": int,
          "total_tokens": int,
          "prompt_tokens_details": {
            "cached_tokens": int
          },
          "completion_tokens_details": {
            "reasoning_tokens": int
          }
        }
      }
    metrics:
      - "Total tokens used"
      - "Cached tokens count"
      - "Completion tokens"
```

## Security and Privacy
```yaml
privacy_features:
  isolation:
    - "Organization-specific caches"
    - "No cross-organization sharing"
  
  data_retention:
    - "Compatible with zero data retention"
    - "Automatic cache clearing"
    - "No manual clearing required"

cost_considerations:
  pricing:
    - "No additional costs"
    - "Automatic optimization"
    - "TPM rate limits apply"
  
  limitations:
    - "Not available on Batch API"
    - "Available on Scale Tier"
    - "Applies to spillover traffic"
```
