# OpenAI Vision API Reference Guide

## Input Methods & Formats
```yaml
input_methods:
  image_url:
    format: |
      {
        "type": "image_url",
        "image_url": {
          "url": "https://example.com/image.jpg",
          "detail": "low|high|auto"
        }
      }
    
  base64:
    format: |
      {
        "type": "image_url",
        "image_url": {
          "url": "data:image/jpeg;base64,{base64_string}",
          "detail": "low|high|auto"
        }
      }

supported_formats:
  - PNG (.png)
  - JPEG (.jpeg, .jpg)
  - WEBP (.webp)
  - GIF (.gif, non-animated)

limitations:
  max_file_size: "20MB per image"
  image_persistence: "Deleted after processing"
```

## Detail Levels & Processing
```yaml
detail_modes:
  low:
    resolution: "512px x 512px"
    token_cost: 85
    use_case: "Fast responses, basic understanding"
    
  high:
    initial_view: "512px x 512px (85 tokens)"
    detailed_crops: "170 tokens per 512px x 512px tile"
    max_dimensions: 
      short_side: "768px"
      long_side: "2000px"
    use_case: "Detailed analysis, text reading"
    
  auto:
    behavior: "Selects low/high based on input size"
    default: true

image_processing:
  high_detail_scaling:
    max_boundary: "2048x2048 square"
    scaling_rules:
      - "Maintain aspect ratio"
      - "Scale shortest side to 768px"
      - "Divide into 512px squares"
```

## Token Cost Calculation
```python
class TokenCalculator:
    def calculate_tokens(self, image_dimensions, detail_level):
        if detail_level == "low":
            return 85
        
        # High detail calculation
        width, height = self._scale_dimensions(image_dimensions)
        num_tiles = self._calculate_tiles(width, height)
        return (170 * num_tiles) + 85

    def _scale_dimensions(self, dimensions):
        width, height = dimensions
        # Scale to fit within 2048x2048
        if width > 2048 or height > 2048:
            scale = min(2048/width, 2048/height)
            width *= scale
            height *= scale
        
        # Scale shortest side to 768px
        scale = 768 / min(width, height)
        return width * scale, height * scale

    def _calculate_tiles(self, width, height):
        return ceil(width/512) * ceil(height/512)
```

## Implementation Examples
```python
# Basic Vision Query
def analyze_image(image_url, prompt):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                        "detail": "auto"
                    }
                }
            ]
        }],
        max_tokens=300
    )

# Multiple Image Analysis
def compare_images(image_urls, prompt):
    content = [{"type": "text", "text": prompt}]
    for url in image_urls:
        content.append({
            "type": "image_url",
            "image_url": {"url": url}
        })
    
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}]
    )

# Base64 Image Upload
def analyze_local_image(image_path, prompt):
    base64_image = encode_image(image_path)
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }]
    )
```

## Known Limitations
```yaml
capability_limitations:
  medical_images:
    status: "Not suitable"
    reason: "Not trained for medical diagnosis"
  
  non_english_text:
    status: "Limited support"
    affected: "Non-Latin alphabets (Japanese, Korean, etc.)"
  
  text_processing:
    small_text: "May struggle with small text"
    rotated_text: "Poor performance with rotated/upside-down text"
    
  visual_elements:
    graphs: "Limited understanding of complex visual elements"
    colors: "May struggle with color-dependent information"
    
  spatial_understanding:
    precision: "Limited spatial reasoning capabilities"
    examples:
      - "Chess positions"
      - "Object location queries"
      
  image_types:
    problematic:
      - "Panoramic images"
      - "Fisheye images"
      - "CAPTCHAs (blocked)"

  metadata:
    supported: false
    details: "No access to original file names or metadata"
```

## Best Practices
```yaml
optimization_strategies:
  image_preparation:
    - "Downsize images before upload"
    - "Ensure clear, well-lit images"
    - "Optimize image resolution for detail level"
    
  performance:
    - "Use URLs for long conversations"
    - "Pre-process images to optimal dimensions"
    - "Choose appropriate detail level"
    
  token_management:
    - "Calculate token costs beforehand"
    - "Monitor rate limits"
    - "Use low detail for basic tasks"

  error_handling:
    - "Validate image formats"
    - "Check file sizes"
    - "Handle unclear image cases"
```

## Framework Integration Considerations
```yaml
implementation_guidelines:
  state_management:
    - "Implement stateful conversation tracking"
    - "Cache processed images if needed"
    - "Handle image cleanup"
    
  abstraction_layer:
    - "Create uniform interface for vision tasks"
    - "Implement image processing utilities"
    - "Standardize error handling"
    
  optimization:
    - "Implement automatic image resizing"
    - "Create intelligent detail level selection"
    - "Build token usage monitoring"
```
