# OpenAI Realtime API Reference Guide

## Connection Setup
```yaml
websocket_config:
  url: "wss://api.openai.com/v1/realtime"
  query_params:
    model: "gpt-4o-realtime-preview-2024-10-01"
  headers:
    Authorization: "Bearer YOUR_API_KEY"
    OpenAI-Beta: "realtime=v1"

audio_formats:
  pcm:
    sampling_rate: "24kHz"
    channels: 1
    bit_depth: "16-bit"
    endianness: "little-endian"
  g711:
    sampling_rate: "8kHz"
    variants: ["u-law", "a-law"]
```

## State Management
```yaml
session_objects:
  session:
    id: "string"
    object: "realtime.session"
    model: "string"
    voice: "string"
    time_limit: "15 minutes"

  conversation:
    id: "string"
    object: "realtime.conversation"
    items: "array"

  items:
    types:
      - message:
          content: ["text", "audio"]
      - function_call:
          tools: "function definitions"
      - function_call_output:
          responses: "function results"

input_buffer:
  operations:
    - "append"
    - "commit"
    - "clear"
  events:
    - "speech_started"
    - "speech_stopped"
    - "committed"
```

## Event Types
```yaml
client_events:
  session:
    - "session.update"
  buffer:
    - "input_audio_buffer.append"
    - "input_audio_buffer.commit"
    - "input_audio_buffer.clear"
  conversation:
    - "conversation.item.create"
    - "conversation.item.truncate"
    - "conversation.item.delete"
  response:
    - "response.create"
    - "response.cancel"

server_events:
  core:
    - "error"
    - "session.created"
    - "session.updated"
    - "conversation.created"
  buffer:
    - "input_audio_buffer.committed"
    - "input_audio_buffer.cleared"
    - "input_audio_buffer.speech_started"
    - "input_audio_buffer.speech_stopped"
  conversation:
    - "conversation.item.created"
    - "conversation.item.truncated"
    - "conversation.item.deleted"
  transcription:
    - "conversation.item.input_audio_transcription.completed"
    - "conversation.item.input_audio_transcription.failed"
  response:
    - "response.created"
    - "response.done"
    - "response.output_item.added"
    - "response.output_item.done"
    - "response.content_part.added"
    - "response.content_part.done"
  content:
    - "response.text.delta"
    - "response.text.done"
    - "response.audio_transcript.delta"
    - "response.audio_transcript.done"
    - "response.audio.delta"
    - "response.audio.done"
  function:
    - "response.function_call_arguments.delta"
    - "response.function_call_arguments.done"
  limits:
    - "rate_limits.updated"
```

## Implementation Examples
```python
# WebSocket Connection
def establish_connection():
    ws = WebSocket(
        url="wss://api.openai.com/v1/realtime",
        params={"model": "gpt-4o-realtime-preview-2024-10-01"},
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "OpenAI-Beta": "realtime=v1"
        }
    )
    return ws

# Audio Message Processing
def process_audio(audio_bytes):
    # Convert to 24kHz mono PCM
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    pcm_audio = (
        audio.set_frame_rate(24000)
        .set_channels(1)
        .set_sample_width(2)
        .raw_data
    )
    return base64.b64encode(pcm_audio).decode()

# Error Handler
class ErrorHandler:
    def handle_error(self, error):
        error_types = {
            "invalid_input": self.handle_invalid_input,
            "model_response_failure": self.handle_model_failure,
            "content_filter": self.handle_content_filter
        }
        handler = error_types.get(error.type, self.handle_unknown)
        return handler(error)
```

## Best Practices
```yaml
implementation:
  audio_handling:
    - "Pre-process audio to correct format"
    - "Implement buffering for streaming"
    - "Handle audio interruptions"
    - "Monitor audio quality"
  
  error_handling:
    - "Watch for error event type"
    - "Surface errors to users"
    - "Implement retry logic"
    - "Log errors for debugging"

  session_management:
    - "Handle 15-minute limit"
    - "Monitor context window"
    - "Implement conversation history"
    - "Handle disconnections"

  moderation:
    - "Include guardrails in instructions"
    - "Check text before audio playback"
    - "Implement content filters"
    - "Monitor output quality"
```

## Performance Optimization
```yaml
optimization_strategies:
  latency:
    - "Use efficient audio formats"
    - "Implement client-side buffering"
    - "Monitor network conditions"
    - "Handle disconnections gracefully"
  
  reliability:
    - "Implement error recovery"
    - "Monitor session health"
    - "Track rate limits"
    - "Handle timeouts"

  monitoring:
    - "Track audio quality"
    - "Monitor response times"
    - "Log error rates"
    - "Track session metrics"
```
