# OpenAI Moderation API Reference

## Model Specifications
```yaml
models:
  omni-moderation-latest:
    features:
      - "Text and image moderation"
      - "Expanded category set"
      - "Input type tracking"
      - "Multi-modal support"
    recommended: "For all new applications"
    response_format: "JSON with detailed category scoring"

  text-moderation-latest:
    features:
      - "Text-only moderation"
      - "Basic category set"
    status: "Legacy"
    use_case: "Text-only applications"
```

## Content Categories
```yaml
harassment:
  description: "Harassing language towards any target"
  models: "All"
  inputs: "Text only"
  subtypes:
    threatening:
      description: "Harassment with violence/serious harm"
      models: "All"
      inputs: "Text only"

hate:
  description: "Content promoting hate based on protected characteristics"
  models: "All"
  inputs: "Text only"
  protected_characteristics:
    - "race"
    - "gender"
    - "ethnicity"
    - "religion"
    - "nationality"
    - "sexual orientation"
    - "disability status"
    - "caste"
  subtypes:
    threatening:
      description: "Hate with violence/serious harm"
      models: "All"
      inputs: "Text only"

illicit:
  description: "Content promoting non-violent wrongdoing"
  models: "Omni only"
  inputs: "Text only"
  subtypes:
    violent:
      description: "Illicit content with violence/weapons"
      models: "Omni only"
      inputs: "Text only"

self_harm:
  description: "Content promoting/depicting self-harm"
  models: "All"
  inputs: "Text and image"
  subtypes:
    intent:
      description: "Expression of self-harm intent"
      models: "All"
      inputs: "Text and image"
    instructions:
      description: "Self-harm instructions/advice"
      models: "All"
      inputs: "Text and image"

sexual:
  description: "Sexually arousing content or services"
  models: "All"
  inputs: "Text and image"
  subtypes:
    minors:
      description: "Sexual content involving minors"
      models: "All"
      inputs: "Text only"

violence:
  description: "Content depicting death/violence/injury"
  models: "All"
  inputs: "Text and images"
  subtypes:
    graphic:
      description: "Graphic depiction of violence"
      models: "All"
      inputs: "Text and images"
```

## Response Structure
```yaml
response_format:
  flagged:
    type: "boolean"
    description: "Overall harmful content detection"
    
  categories:
    type: "object"
    description: "Per-category violation flags"
    values: "boolean"
    
  category_scores:
    type: "object"
    description: "Confidence scores per category"
    range: "0.0 to 1.0"
    
  category_applied_input_types:
    type: "object"
    description: "Input types flagged per category"
    values: ["text", "image"]
    availability: "Omni models only"
```

## Implementation Examples
```python
# Basic Text Moderation
def moderate_text(text):
    return client.moderations.create(
        model="omni-moderation-latest",
        input=text
    )

# Multi-Input Moderation
def moderate_content(text=None, image=None):
    input_data = {}
    if text:
        input_data["text"] = text
    if image:
        input_data["image"] = image
        
    return client.moderations.create(
        model="omni-moderation-latest",
        **input_data
    )

# Category-Specific Moderation
def check_specific_categories(content, categories):
    response = client.moderations.create(
        model="omni-moderation-latest",
        input=content
    )
    
    return {
        category: response.results[0].category_scores[category]
        for category in categories
    }
```

## Best Practices
```yaml
implementation:
  input_handling:
    - "Validate input formats"
    - "Handle multi-modal content appropriately"
    - "Implement proper error handling"
    
  response_processing:
    - "Consider confidence thresholds"
    - "Handle all categories appropriately"
    - "Implement proper logging"
    
  performance:
    - "Batch processing when possible"
    - "Implement caching for repeated checks"
    - "Monitor API usage"

content_policy:
  enforcement:
    - "Define clear violation thresholds"
    - "Implement graduated response actions"
    - "Document enforcement policies"
    
  user_communication:
    - "Provide clear feedback"
    - "Implement appeals process"
    - "Maintain transparency"
```

## Framework Integration Considerations
```yaml
integration_patterns:
  preprocessing:
    - "Content normalization"
    - "Input validation"
    - "Format conversion"
    
  response_handling:
    - "Category-specific actions"
    - "Confidence threshold management"
    - "Violation tracking"
    
  monitoring:
    - "API usage tracking"
    - "Error rate monitoring"
    - "Category distribution analysis"
    
  logging:
    - "Decision logging"
    - "Violation tracking"
    - "Audit trail maintenance"
```

## Error Handling
```yaml
error_types:
  input_errors:
    - "Invalid input format"
    - "Content size limits"
    - "Unsupported content types"
    
  api_errors:
    - "Rate limits"
    - "Authentication issues"
    - "Service availability"
    
  content_errors:
    - "Unprocessable content"
    - "Corrupted inputs"
    - "Invalid encodings"

error_responses:
  strategies:
    - "Retry with exponential backoff"
    - "Fallback to alternative processing"
    - "User notification"
```
