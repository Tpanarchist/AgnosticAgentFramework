# OpenAI Speech-to-Text API Reference Guide

## API Endpoints
```yaml
endpoints:
  transcriptions:
    purpose: "Transcribe audio in original language"
    model: "whisper-1"
    input_limit: "25 MB"
    supported_formats: 
      - "mp3"
      - "mp4"
      - "mpeg"
      - "mpga"
      - "m4a"
      - "wav"
      - "webm"

  translations:
    purpose: "Translate audio to English"
    model: "whisper-1"
    input_limit: "25 MB"
    supported_formats: 
      - "mp3"
      - "mp4"
      - "mpeg"
      - "mpga"
      - "m4a"
      - "wav"
      - "webm"
    output_language: "English only"
```

## Implementation Examples
```python
# Basic Transcription
def transcribe_audio(file_path, format="json"):
    audio_file = open(file_path, "rb")
    return client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format=format
    )

# Translation to English
def translate_audio(file_path):
    audio_file = open(file_path, "rb")
    return client.audio.translations.create(
        model="whisper-1",
        file=audio_file
    )

# Timestamped Transcription
def transcribe_with_timestamps(file_path):
    audio_file = open(file_path, "rb")
    return client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"]
    )

# Handling Long Audio Files
def split_and_transcribe(file_path, segment_length=600000):  # 10 minutes
    from pydub import AudioSegment
    
    audio = AudioSegment.from_mp3(file_path)
    segments = len(audio) // segment_length + 1
    transcripts = []
    
    for i in range(segments):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(audio))
        segment = audio[start:end]
        
        # Export segment to temporary file
        temp_path = f"segment_{i}.mp3"
        segment.export(temp_path, format="mp3")
        
        # Transcribe segment
        transcript = transcribe_audio(temp_path)
        transcripts.append(transcript)
    
    return transcripts
```

## Response Formats
```yaml
response_options:
  json:
    default: true
    format: |
      {
        "text": "transcribed text here"
      }

  text:
    format: "Raw text output"

  verbose_json:
    format: |
      {
        "task": "transcribe",
        "language": "en",
        "duration": 2.95,
        "text": "transcribed text",
        "segments": [...],
        "words": [...]
      }
```

## Language Support
```yaml
supported_languages:
  performance_tier:
    high_quality: # >50% Word Error Rate (WER)
      european:
        - "English"
        - "French"
        - "German"
        - "Italian"
        - "Spanish"
        # ... [other European languages]
      asian:
        - "Japanese"
        - "Korean"
        - "Chinese"
        # ... [other Asian languages]
      other:
        - "Arabic"
        - "Hindi"
        # ... [other languages]
    
  notes:
    - "Model trained on 98 languages total"
    - "Listed languages exceeded 50% WER benchmark"
    - "Unlisted languages may have lower quality results"
```

## Prompting and Enhancement
```yaml
prompting_strategies:
  acronym_correction:
    example: "Transcript includes OpenAI products like DALL·E, GPT-3"
    use_case: "Improve recognition of specific terms"

  context_preservation:
    technique: "Include previous segment transcript"
    limitation: "Only last 224 tokens considered"

  punctuation_improvement:
    example: "Hello, welcome to my lecture."
    use_case: "Enforce proper punctuation"

  filler_word_retention:
    example: "Umm, let me think like, hmm..."
    use_case: "Preserve speech patterns"

enhancement_methods:
  prompt_parameter:
    max_length: "244 tokens"
    use_case: "Small dictionary of terms"
    example: |
      prompt="ZyntriQix, Digique Plus, CynapseFive"

  gpt4_post_processing:
    advantages:
      - "Larger context window"
      - "Better instruction following"
      - "More reliable corrections"
```

## Best Practices
```yaml
audio_preparation:
  file_handling:
    - "Keep files under 25 MB"
    - "Use compressed formats when possible"
    - "Maintain audio quality"
    - "Avoid mid-sentence splits"

  segmentation:
    - "Split long audio files strategically"
    - "Preserve context between segments"
    - "Implement proper segment overlap"

  quality_optimization:
    - "Use high-quality audio sources"
    - "Minimize background noise"
    - "Ensure clear speech"

error_handling:
  strategies:
    - "Validate file formats"
    - "Handle timeouts for long files"
    - "Implement retry logic"
    - "Monitor API response codes"
```

## Framework Integration Considerations
```yaml
integration_patterns:
  audio_processing:
    - "Implement file format validation"
    - "Handle audio splitting utilities"
    - "Manage temporary files"
    - "Process response formats"

  error_handling:
    - "Handle API errors"
    - "Manage rate limits"
    - "Process partial results"
    - "Implement fallback strategies"

  optimization:
    - "Cache common transcriptions"
    - "Implement batch processing"
    - "Monitor resource usage"
    - "Track performance metrics"

  quality_assurance:
    - "Validate transcription quality"
    - "Monitor word error rates"
    - "Track language performance"
    - "Log enhancement results"
```
