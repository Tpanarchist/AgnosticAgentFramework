# OpenAI Structured Outputs Reference Guide

## Model Support
```yaml
supported_models:
  current:
    - "gpt-4o-mini-2024-07-18 and later"
    - "gpt-4o-2024-08-06 and later"
  features:
    - "Schema adherence"
    - "Type safety"
    - "Explicit refusals"
    - "Simplified prompting"

json_mode_alternatives:
  models:
    - "gpt-3.5-turbo"
    - "gpt-4-*"
    - "gpt-4o-*"
  features:
    - "Valid JSON output"
    - "No schema adherence"
    - "Basic format validation"
```

## Schema Support and Limitations
```yaml
supported_types:
  basic:
    - "string"
    - "number"
    - "boolean"
    - "integer"
    - "object"
    - "array"
    - "enum"
    - "anyOf"
  
  limitations:
    object_constraints:
      max_properties: 100
      max_nesting_levels: 5
      required: "All fields must be required"
      additional_properties: "Must be false"

  unsupported_keywords:
    strings:
      - "minLength"
      - "maxLength"
      - "pattern"
      - "format"
    numbers:
      - "minimum"
      - "maximum"
      - "multipleOf"
    objects:
      - "patternProperties"
      - "unevaluatedProperties"
      - "propertyNames"
      - "minProperties"
      - "maxProperties"
    arrays:
      - "unevaluatedItems"
      - "contains"
      - "minContains"
      - "maxContains"
      - "minItems"
      - "maxItems"
      - "uniqueItems"
```

## Implementation Examples
```python
# Basic Schema Definition
class ResponseSchema(BaseModel):
    name: str
    age: int
    email: str

# Function Using Schema
def get_structured_response(prompt: str, schema: Type[BaseModel]):
    response = client.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Extract structured information."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format=schema
    )
    return response.choices[0].message.parsed

# Handling Optional Fields
class OptionalSchema(BaseModel):
    required_field: str
    optional_field: Optional[str]
    nullable_field: Union[str, None]

# Recursive Schema Example
class RecursiveNode(BaseModel):
    value: str
    children: Optional[List['RecursiveNode']]
```

## Response Handling
```python
class StructuredResponseHandler:
    def process_response(self, response):
        message = response.choices[0].message
        
        if message.parsed:
            return self.handle_parsed_response(message.parsed)
        elif message.refusal:
            return self.handle_refusal(message.refusal)
        
        return self.handle_error("Invalid response format")
    
    def handle_parsed_response(self, parsed_data):
        try:
            # Validate against schema
            validated_data = self.schema.validate(parsed_data)
            return validated_data
        except ValidationError as e:
            return self.handle_validation_error(e)
    
    def handle_refusal(self, refusal):
        # Log and handle model refusal
        return {
            "status": "refused",
            "reason": refusal
        }

    def handle_error(self, error_msg):
        return {
            "status": "error",
            "message": error_msg
        }
```

## Best Practices
```yaml
schema_design:
  naming:
    - "Use clear, descriptive field names"
    - "Follow language naming conventions"
    - "Include units in field names when relevant"
  
  structure:
    - "Keep nesting depth minimal"
    - "Group related fields logically"
    - "Use enums for constrained values"
    - "Design for extensibility"

error_handling:
  validation:
    - "Implement schema validation"
    - "Handle missing required fields"
    - "Validate data types"
    - "Check value constraints"
  
  refusals:
    - "Handle model refusals gracefully"
    - "Provide meaningful feedback"
    - "Log refusal reasons"
    - "Implement retry strategies"

performance:
  optimization:
    - "Cache schema validations"
    - "Minimize schema complexity"
    - "Batch related requests"
    - "Monitor parsing overhead"
```

## Integration Guidelines
```yaml
implementation_patterns:
  type_safety:
    - "Use native language type systems"
    - "Implement schema validation"
    - "Handle type conversions"
    - "Validate before processing"

  schema_management:
    - "Version control schemas"
    - "Maintain schema documentation"
    - "Track schema changes"
    - "Validate schema compatibility"

  error_handling:
    - "Implement robust validation"
    - "Handle parsing errors"
    - "Process refusals gracefully"
    - "Log validation failures"
```

## Migration from JSON Mode
```yaml
transition_steps:
  assessment:
    - "Identify JSON mode usage"
    - "Analyze schema requirements"
    - "Evaluate model compatibility"
    - "Plan migration timeline"

  implementation:
    - "Define structured schemas"
    - "Update API calls"
    - "Implement validation"
    - "Test schema compliance"

  validation:
    - "Verify schema adherence"
    - "Test edge cases"
    - "Monitor error rates"
    - "Compare performance metrics"
```
