# Model Selection Guide

## Core Principles
```yaml
selection_hierarchy:
  primary:
    focus: "Accuracy"
    priority: "Meet accuracy targets first"
    rationale: "Invalid results make cost/latency irrelevant"
    
  secondary:
    focus: ["Cost", "Latency"]
    priority: "Optimize after accuracy achieved"
    approach: "Maintain accuracy with minimal resources"

accuracy_optimization:
  target_setting:
    requirements:
      - "Clear accuracy metrics"
      - "Evaluation dataset"
      - "Performance thresholds"
    example: |
      {
        "metric": "Triage accuracy",
        "target": "90% correct first-time",
        "evaluation": "100 sample interactions"
      }

  methods:
    start_point: "Most capable model"
    techniques:
      - "Retrieval-augmented generation"
      - "Fine-tuning optimization"
      - "Prompt engineering"
    data_collection:
      - "Log all responses"
      - "Save prompt-completion pairs"
      - "Build evaluation datasets"
```

## ROI Calculations
```yaml
accuracy_targeting:
  example_calculation:
    correct_classification:
      cost_saving: "$50 per case"
      benefit: "Avoided human review"
    
    incorrect_classification:
      cost_impact: "$300 per case"
      consequences:
        - "Review process triggered"
        - "Complaint handling"
        - "Reputation impact"

    breakeven_calculation:
      formula: |
        Breakeven = Cost_incorrect / (Cost_incorrect + Savings_correct)
      example:
        calculation: "$300 / ($300 + $50)"
        result: "85.8% accuracy needed"
      target: "90% for ROI safety margin"
```

## Optimization Strategies
```yaml
cost_latency_optimization:
  approaches:
    model_comparison:
      method: "Zero/few-shot with smaller models"
      goal: "Maintain accuracy at lower cost"
      
    model_distillation:
      method: "Fine-tune smaller model"
      input: "Data from accuracy optimization"

  reduction_strategies:
    requests:
      - "Combine related queries"
      - "Implement caching"
      - "Batch processing"
    
    tokens:
      - "Optimize prompt length"
      - "Control response length"
      - "Efficient formatting"

    model_size:
      - "Test smaller models"
      - "Balance capabilities"
      - "Monitor performance"
```

## Implementation Example
```yaml
fake_news_classifier:
  targets:
    accuracy: "90% correct classification"
    cost: "<$5 per 1000 articles"
    latency: "<2 seconds per article"

  experiments:
    zero_shot:
      model: "gpt-4o"
      accuracy: "84.5%"
      cost: "$1.72"
      latency: "<1s"
      results: "Missed accuracy target"

    few_shot:
      model: "gpt-4o"
      examples: 5
      accuracy: "91.5%"
      cost: "$11.92"
      latency: "<1s"
      results: "Met accuracy, exceeded cost"

    fine_tuned:
      model: "gpt-4o-mini"
      training_examples: 1000
      accuracy: "91.5%"
      cost: "$0.21"
      latency: "<1s"
      results: "Met all targets"
```

## Best Practices
```yaml
implementation_guidelines:
  initial_setup:
    - "Define clear accuracy metrics"
    - "Create evaluation datasets"
    - "Set performance thresholds"
    - "Implement logging systems"

  optimization_process:
    accuracy:
      - "Start with most capable model"
      - "Log all interactions"
      - "Build training datasets"
      - "Validate results"
    
    cost_latency:
      - "Test smaller models"
      - "Implement fine-tuning"
      - "Monitor performance metrics"
      - "Balance trade-offs"

  monitoring:
    metrics:
      - "Accuracy rates"
      - "Cost per operation"
      - "Response latency"
      - "Error patterns"
```

## Special Considerations
```yaml
exception_cases:
  cost_sensitive:
    approach: "Set cost threshold first"
    strategy: "Optimize within budget"
    
  latency_critical:
    approach: "Set latency requirements first"
    strategy: "Filter compatible models"
    
  high_accuracy:
    approach: "Start with largest model"
    strategy: "Only reduce if targets met"

tradeoff_management:
  priorities:
    - "Accuracy requirements"
    - "Budget constraints"
    - "Speed requirements"
  balance:
    - "Test multiple approaches"
    - "Document trade-offs"
    - "Regular re-evaluation"
```
