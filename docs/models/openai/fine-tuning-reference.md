# OpenAI Fine-tuning API Reference Guide

## Model Support
```yaml
supported_models:
  gpt4_series:
    - model: "gpt-4o-2024-08-06"
      context_window: "128,000 tokens"
      training_window: "65,536 tokens"
    - model: "gpt-4o-mini-2024-07-18"
      context_window: "128,000 tokens" 
      training_window: "65,536 tokens"
    - model: "gpt-4-0613"
      context_window: "8,192 tokens"
      training_window: "8,192 tokens"

  gpt35_series:
    - model: "gpt-3.5-turbo-0125"
      context_window: "16,385 tokens"
      training_window: "16,385 tokens"
    - model: "gpt-3.5-turbo-1106"
      context_window: "16,385 tokens"
      training_window: "16,385 tokens"
    - model: "gpt-3.5-turbo-0613"
      context_window: "4,096 tokens"
      training_window: "4,096 tokens"

  base_models:
    - model: "babbage-002"
      deprecation: "October 28, 2024"
    - model: "davinci-002"
      deprecation: "October 28, 2024"
```

## Training Data Format
```yaml
chat_format:
  structure: |
    {
      "messages": [
        {
          "role": "system",
          "content": "string"
        },
        {
          "role": "user",
          "content": "string"
        },
        {
          "role": "assistant",
          "content": "string",
          "weight": 0|1  # Optional, for controlling training
        }
      ]
    }

  multimodal_support:
    images:
      limits:
        max_examples: 50000
        max_images_per_example: 10
        max_image_size: "10 MB"
      formats:
        - "JPEG"
        - "PNG"
        - "WEBP"
      modes:
        - "RGB"
        - "RGBA"
      restrictions:
        - "No people/faces"
        - "No CAPTCHAs"
        - "No assistant role images"
```

## Implementation Examples
```python
# Data Validation
def validate_training_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            example = json.loads(line)
            validate_messages(example['messages'])
            if 'tools' in example:
                validate_tools(example['tools'])

# File Upload
def upload_training_file(file_path):
    return client.files.create(
        file=open(file_path, "rb"),
        purpose="fine-tune"
    )

# Create Fine-tuning Job
def create_fine_tuning_job(
    training_file_id,
    model="gpt-4o-mini",
    hyperparameters=None
):
    return client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model=model,
        hyperparameters=hyperparameters
    )

# Job Management
class FineTuningManager:
    def list_jobs(self, limit=10):
        return client.fine_tuning.jobs.list(limit=limit)
    
    def get_job_status(self, job_id):
        return client.fine_tuning.jobs.retrieve(job_id)
    
    def cancel_job(self, job_id):
        return client.fine_tuning.jobs.cancel(job_id)
    
    def list_events(self, job_id, limit=10):
        return client.fine_tuning.jobs.list_events(
            fine_tuning_job_id=job_id,
            limit=limit
        )
```

## Hyperparameters
```yaml
tunable_parameters:
  n_epochs:
    description: "Number of training epochs"
    when_to_increase:
      - "Model not following training data enough"
      - "Tasks with single ideal completion"
    when_to_decrease:
      - "Model becomes less diverse"
      - "Tasks with multiple valid completions"

  learning_rate_multiplier:
    description: "Controls step size during training"
    when_to_adjust: "Model not converging"

  batch_size:
    description: "Number of training examples processed together"
    considerations: 
      - "Affects training stability"
      - "Memory usage"
```

## Best Practices
```yaml
data_preparation:
  quality:
    - "Review examples for consistency"
    - "Include edge cases"
    - "Balance dataset distribution"
    - "Validate format and content"
    
  quantity:
    minimum: 10
    recommended: "50-100"
    scaling: "Double dataset to estimate improvements"

error_handling:
  validation:
    - "Check data format"
    - "Verify token counts"
    - "Monitor training metrics"
    - "Test model outputs"

  monitoring:
    - "Track training progress"
    - "Compare with base model"
    - "Evaluate on test set"
    - "Monitor costs"
```

## Integration Patterns
```yaml
wandb_integration:
  authentication:
    required: "W&B API key in Account Dashboard"
    permissions: "Account administrators only"
    
  configuration:
    job_creation: |
      {
        "integrations": [{
          "type": "wandb",
          "wandb": {
            "project": "string",
            "tags": ["string"],
            "name": "string"  # Optional
          }
        }]
      }
    
  tracking:
    metrics:
      - "Training loss"
      - "Validation loss"
      - "Token accuracy"
      - "Hyperparameters"
      
    visualization:
      - "Learning curves"
      - "Performance metrics"
      - "Resource usage"
```

## Cost Management
```yaml
cost_calculation:
  formula: |
    (base_cost_per_1M_tokens / 1M) * 
    input_tokens * 
    n_epochs

  optimization:
    - "Use gpt-4o-mini for most cases"
    - "Optimize token usage"
    - "Monitor training duration"
    - "Track resource usage"
```
