# OpenAI Models Catalog Reference

## GPT-4o Models (Omni)
```yaml
gpt-4o:
  current_pointer: "gpt-4o-2024-08-06"
  variants:
    base:
      name: "gpt-4o"
      context_window: 128000
      max_output_tokens: 16384
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "gpt-4o-2024-08-06"
        context_window: 128000
        max_output_tokens: 16384
        features: ["Structured Outputs"]
      - name: "gpt-4o-2024-05-13"
        context_window: 128000
        max_output_tokens: 4096
    research:
      name: "chatgpt-4o-latest"
      context_window: 128000
      max_output_tokens: 16384
      note: "Dynamic model for research/evaluation"
  capabilities:
    - Text input/output
    - Image input
    - Advanced reasoning
    - Multilingual
    - Vision tasks

gpt-4o-mini:
  current_pointer: "gpt-4o-mini-2024-07-18"
  variants:
    base:
      name: "gpt-4o-mini"
      context_window: 128000
      max_output_tokens: 16384
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "gpt-4o-mini-2024-07-18"
        context_window: 128000
        max_output_tokens: 16384
  capabilities:
    - Text input/output
    - Image input
    - Fast processing
    - Cost-effective
    - Vision tasks

gpt-4o-realtime:
  variants:
    preview:
      name: "gpt-4o-realtime-preview"
      context_window: 128000
      max_output_tokens: 4096
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "gpt-4o-realtime-preview-2024-10-01"
        context_window: 128000
        max_output_tokens: 4096
  capabilities:
    - Audio input
    - Text input/output
    - WebSocket interface
    - Realtime processing

gpt-4o-audio:
  variants:
    preview:
      name: "gpt-4o-audio-preview"
      context_window: 128000
      max_output_tokens: 16384
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "gpt-4o-audio-preview-2024-10-01"
        context_window: 128000
        max_output_tokens: 16384
  capabilities:
    - Audio input
    - Text output
    - Chat completions
```

## O1 Reasoning Models (Beta)
```yaml
o1-preview:
  current_pointer: "o1-preview-2024-09-12"
  variants:
    base:
      name: "o1-preview"
      context_window: 128000
      max_output_tokens: 32768
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "o1-preview-2024-09-12"
        context_window: 128000
        max_output_tokens: 32768
  capabilities:
    - Complex reasoning
    - Chain-of-thought processing
    - Problem solving
    - Text input/output

o1-mini:
  current_pointer: "o1-mini-2024-09-12"
  variants:
    base:
      name: "o1-mini"
      context_window: 128000
      max_output_tokens: 65536
      training_cutoff: "Oct 2023"
    snapshots:
      - name: "o1-mini-2024-09-12"
        context_window: 128000
        max_output_tokens: 65536
  capabilities:
    - Coding tasks
    - Mathematical reasoning
    - Scientific analysis
    - Faster processing
```

## GPT-4 and GPT-4 Turbo Models
```yaml
gpt-4-turbo:
  current_pointer: "gpt-4-turbo-2024-04-09"
  variants:
    base:
      name: "gpt-4-turbo"
      context_window: 128000
      max_output_tokens: 4096
      training_cutoff: "Dec 2023"
    preview:
      name: "gpt-4-turbo-preview"
      context_window: 128000
      max_output_tokens: 4096
    snapshots:
      - name: "gpt-4-turbo-2024-04-09"
        context_window: 128000
        max_output_tokens: 4096
        features: ["Vision", "JSON mode", "Function calling"]
      - name: "gpt-4-0125-preview"
        context_window: 128000
        max_output_tokens: 4096
      - name: "gpt-4-1106-preview"
        context_window: 128000
        max_output_tokens: 4096
  capabilities:
    - Text generation
    - Vision tasks
    - Function calling
    - JSON mode

gpt-4:
  current_pointer: "gpt-4-0613"
  variants:
    base:
      name: "gpt-4"
      context_window: 8192
      max_output_tokens: 8192
      training_cutoff: "Sep 2021"
    snapshots:
      - name: "gpt-4-0613"
        context_window: 8192
        max_output_tokens: 8192
        features: ["Function calling"]
      - name: "gpt-4-0314"
        context_window: 8192
        max_output_tokens: 8192
  capabilities:
    - Text generation
    - Complex reasoning
    - Code generation
```

## GPT-3.5 Turbo Models
```yaml
gpt-3.5-turbo:
  current_pointer: "gpt-3.5-turbo-0125"
  variants:
    base:
      name: "gpt-3.5-turbo"
      context_window: 16385
      max_output_tokens: 4096
      training_cutoff: "Sep 2021"
    snapshots:
      - name: "gpt-3.5-turbo-0125"
        context_window: 16385
        max_output_tokens: 4096
      - name: "gpt-3.5-turbo-1106"
        context_window: 16385
        max_output_tokens: 4096
        features: ["JSON mode", "Function calling"]
    instruct:
      name: "gpt-3.5-turbo-instruct"
      context_window: 4096
      max_output_tokens: 4096
  capabilities:
    - Text generation
    - Chat optimization
    - Basic tasks
```

## Specialized Models
```yaml
dall_e:
  variants:
    - name: "dall-e-3"
      description: "Latest DALL·E model (Nov 2023)"
      capabilities: ["Image generation from text"]
    - name: "dall-e-2"
      description: "Previous DALL·E model (Nov 2022)"
      capabilities: ["Image generation", "Image editing", "Variations"]

tts:
  variants:
    - name: "tts-1"
      description: "Text to speech, optimized for speed"
      capabilities: ["Real-time text to speech"]
    - name: "tts-1-hd"
      description: "Text to speech, optimized for quality"
      capabilities: ["High-quality speech synthesis"]

whisper:
  variants:
    - name: "whisper-1"
      description: "Speech recognition model"
      capabilities:
        - Multilingual speech recognition
        - Speech translation
        - Language identification

embeddings:
  variants:
    - name: "text-embedding-3-large"
      dimensions: 3072
      capabilities: ["Text embeddings", "Multilingual support"]
    - name: "text-embedding-3-small"
      dimensions: 1536
      capabilities: ["Text embeddings", "Efficient processing"]
    - name: "text-embedding-ada-002"
      dimensions: 1536
      capabilities: ["Legacy text embeddings"]

moderation:
  variants:
    - name: "omni-moderation-latest"
      current_pointer: "omni-moderation-2024-09-26"
      max_tokens: 32768
      capabilities: ["Text moderation", "Image moderation"]
    - name: "text-moderation-latest"
      current_pointer: "text-moderation-007"
      max_tokens: 32768
      capabilities: ["Text-only moderation"]
```

## Base GPT Models
```yaml
base_models:
  variants:
    - name: "babbage-002"
      context_window: 16384
      training_cutoff: "Sep 2021"
      description: "Replacement for GPT-3 ada and babbage"
      
    - name: "davinci-002"
      context_window: 16384
      training_cutoff: "Sep 2021"
      description: "Replacement for GPT-3 curie and davinci"
```

## Model Deprecation Notes
```yaml
deprecation_policy:
  pinned_versions: "3 months minimum after new version"
  notification: "Advance notice provided"
  migration_path: "Always specified with deprecation notice"
```
