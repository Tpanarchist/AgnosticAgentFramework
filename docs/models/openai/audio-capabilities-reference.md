# OpenAI Audio API Reference Guide

## Modality Support Matrix
```yaml
gpt4o_audio_preview:
  supported_combinations:
    text_to_audio:
      input: "text"
      output: ["text", "audio"]
    
    audio_to_both:
      input: "audio"
      output: ["text", "audio"]
    
    audio_to_text:
      input: "audio"
      output: ["text"]
    
    mixed_to_both:
      input: ["text", "audio"]
      output: ["text", "audio"]
    
    mixed_to_text:
      input: ["text", "audio"]
      output: ["text"]

token_considerations:
  audio_input: "1 hour ≈ 128k tokens"
  context_window: "128k tokens maximum"
```

## Implementation Examples
```python
# Basic Audio Generation
class AudioGenerator:
    def generate_audio_response(self, prompt, voice="alloy", format="wav"):
        return client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={
                "voice": voice,
                "format": format
            },
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
    
    def save_audio_response(self, response, filename):
        wav_bytes = base64.b64decode(response.choices[0].message.audio.data)
        with open(filename, "wb") as f:
            f.write(wav_bytes)

# Multi-turn Conversation Handler
class AudioConversationHandler:
    def continue_conversation(self, messages, new_prompt):
        return client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[*messages, {
                "role": "user",
                "content": new_prompt
            }]
        )
    
    def format_assistant_audio_message(self, audio_id):
        return {
            "role": "assistant",
            "audio": {
                "id": audio_id
            }
        }
```

## Response Structure
```yaml
audio_response:
  format: |
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "refusal": null,
        "audio": {
          "id": "audio_abc123",
          "expires_at": "unix_timestamp",
          "data": "base64_encoded_bytes",
          "transcript": "text_transcript"
        }
      },
      "finish_reason": "stop"
    }

audio_properties:
  id: "Unique identifier for multi-turn conversations"
  expires_at: "Unix timestamp for audio expiration"
  data: "Base64 encoded audio data"
  transcript: "Text transcription of audio content"
```

## Audio Configuration Options
```yaml
output_settings:
  voices:
    - "alloy"    # Default voice
    # Additional voices TBD
    
  formats:
    - "wav"      # Standard WAV format
    # Additional formats TBD

input_requirements:
  audio_length: "Limited by token context window (≈1 hour)"
  supported_formats: TBD
  quality_requirements: TBD
```

## Function/Tool Calling Support
```yaml
tool_calling:
  compatibility: "Standard Chat Completions API tool calling"
  implementation: |
    {
      "model": "gpt-4o-audio-preview",
      "modalities": ["text", "audio"],
      "audio": {"voice": "alloy", "format": "wav"},
      "messages": [...],
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "description": "Get current weather",
            "parameters": {...}
          }
        }
      ]
    }
```

## Best Practices
```yaml
conversation_management:
  audio_retention:
    - "Store audio IDs for conversation continuity"
    - "Track audio expiration timestamps"
    - "Implement fallback for expired audio"
  
  performance:
    - "Reuse audio IDs for related messages"
    - "Monitor token usage for audio inputs"
    - "Handle audio processing asynchronously"

error_handling:
  strategies:
    - "Validate audio format before sending"
    - "Handle audio processing failures"
    - "Implement retry logic for network issues"
    - "Monitor audio quality issues"

resource_management:
  considerations:
    - "Track token usage for audio inputs"
    - "Implement audio caching strategies"
    - "Monitor audio storage requirements"
    - "Handle audio cleanup"
```

## Framework Integration Considerations
```yaml
audio_integration:
  abstraction_layer:
    - "Unified audio interface for different providers"
    - "Standard audio format conversion utilities"
    - "Common error handling patterns"
    - "Audio quality validation"

  state_management:
    - "Audio session tracking"
    - "Conversation history with audio references"
    - "Audio expiration handling"
    - "Caching strategies"

  optimization:
    - "Audio preprocessing pipeline"
    - "Automatic format conversion"
    - "Quality validation checks"
    - "Resource cleanup routines"

  monitoring:
    - "Audio quality metrics"
    - "Token usage tracking"
    - "Performance monitoring"
    - "Error rate tracking"
```

## Limitations and Considerations
```yaml
current_limitations:
  modality_control:
    - "Limited to predefined modality combinations"
    - "No fine-grained output control"
    
  audio_processing:
    - "Token limit constraints on audio length"
    - "Processing time for longer audio"
    - "Quality dependent on input audio"

  integration:
    - "Stateless API requires manual audio management"
    - "Audio expiration handling needed"
    - "Limited voice selection options"
```
