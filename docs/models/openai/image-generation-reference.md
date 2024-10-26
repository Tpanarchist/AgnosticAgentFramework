# OpenAI Image Generation API Reference

## Model Capabilities Overview
```yaml
dall_e_3:
  features:
    - Text to image generation
    - Enhanced detail mode (HD)
    - Automatic prompt enhancement
  limitations:
    - One image per request
    - No editing or variations
    - No transparency support
  sizes:
    - "1024x1024"   # Square
    - "1024x1792"   # Portrait
    - "1792x1024"   # Landscape
  quality_options:
    - "standard"  # Default, faster
    - "hd"       # Enhanced detail

dall_e_2:
  features:
    - Text to image generation
    - Image editing (inpainting)
    - Image variations
    - Multiple images per request
  limitations:
    - Less detailed than DALL·E 3
    - Square images only
  sizes:
    - "256x256"
    - "512x512"
    - "1024x1024"
  max_images_per_request: 10
```

## API Endpoints
```yaml
endpoints:
  generations:
    path: "/v1/images/generations"
    methods:
      - model: "dall-e-3"
        parameters:
          required:
            - prompt: "string"
            - model: "dall-e-3"
          optional:
            - quality: "standard|hd"
            - size: "1024x1024|1024x1792|1792x1024"
            - style: "natural|vivid"
            - n: 1  # Fixed for DALL-E 3
      - model: "dall-e-2"
        parameters:
          required:
            - prompt: "string"
            - model: "dall-e-2"
          optional:
            - size: "256x256|512x512|1024x1024"
            - n: "1-10"
            - response_format: "url|b64_json"

  edits:  # DALL-E 2 only
    path: "/v1/images/edits"
    parameters:
      required:
        - image: "PNG file"
        - mask: "PNG file with transparency"
        - prompt: "string"
      optional:
        - size: "256x256|512x512|1024x1024"
        - n: "1-10"
        - response_format: "url|b64_json"

  variations:  # DALL-E 2 only
    path: "/v1/images/variations"
    parameters:
      required:
        - image: "PNG file"
      optional:
        - size: "256x256|512x512|1024x1024"
        - n: "1-10"
        - response_format: "url|b64_json"
```

## Implementation Examples
```python
# Image Generation - DALL-E 3
def generate_image(prompt, size="1024x1024", quality="standard"):
    return client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality=quality,
        n=1
    )

# Image Editing - DALL-E 2
def edit_image(image_path, mask_path, prompt):
    return client.images.edit(
        model="dall-e-2",
        image=open(image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt=prompt,
        size="1024x1024"
    )

# Image Variations - DALL-E 2
def create_variation(image_path):
    return client.images.create_variation(
        model="dall-e-2",
        image=open(image_path, "rb"),
        n=1,
        size="1024x1024"
    )
```

## Image Requirements
```yaml
input_image_requirements:
  format: "PNG"
  size_limit: "4MB"
  dimensions: "Square aspect ratio required"
  transparency: 
    edits: "Required in mask for edit areas"
    variations: "Not supported"
  
mask_requirements:
  format: "PNG"
  size: "Must match input image dimensions"
  transparency: "Required to indicate edit areas"
```

## Response Formats
```yaml
response_options:
  url:
    format: "String URL"
    expiration: "1 hour"
    default: true
  
  b64_json:
    format: "Base64 encoded string"
    expiration: "None"
    size_impact: "Larger response payload"
```

## Error Handling
```python
class ImageAPIErrorHandler:
    common_errors = {
        "content_policy": {
            "type": "Prompt or image filtered",
            "resolution": "Modify content to comply with policy"
        },
        "invalid_input": {
            "type": "File format/size/dimension issues",
            "resolution": "Ensure inputs meet requirements"
        },
        "rate_limit": {
            "type": "Too many requests",
            "resolution": "Implement exponential backoff"
        }
    }

    error_handling_pattern = """
    try:
        response = client.images.generate(...)
    except OpenAIError as e:
        if e.response:
            handle_api_error(e.response.status, e.response.data)
        else:
            handle_connection_error(e.message)
    """
```

## Best Practices
```yaml
prompting:
  dall_e_3:
    - Provide clear, detailed descriptions
    - Use the bypass prompt prefix for exact prompts
    - Check revised_prompt in response for actual prompt used
    
  dall_e_2:
    - Be specific and descriptive
    - Include style preferences
    - Specify important details

performance:
  - Cache generated images
  - Implement retry logic
  - Use appropriate size for use case
  - Monitor rate limits

error_handling:
  - Validate inputs before sending
  - Handle all error cases
  - Implement proper logging
  - Provide user feedback

security:
  - Validate input images
  - Implement content filtering
  - Handle user data securely
  - Monitor for abuse
```

## Framework Integration Considerations
```yaml
agnostic_integration:
  abstraction_layer:
    - Unified image generation interface
    - Provider-agnostic response format
    - Common error handling patterns
    - Standardized input validation

  image_processing:
    - Input image validation
    - Format conversion
    - Size and dimension handling
    - Response processing

  caching_strategy:
    - URL response caching
    - Base64 response handling
    - Temporary file management
    - Cache invalidation
```
