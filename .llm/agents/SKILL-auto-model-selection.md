# Agent: Auto-Model Selection

**Priority:** 10
**Suggested Model:** `qwen-3.5-14b`
**Type:** Decision/Analysis Agent

## Description
Analyzes data patterns and recommends the most appropriate forecasting model from the available options. This agent acts as an intelligent selector that evaluates multiple models and provides recommendations.

## When to Use
Use this agent when:
- Unsure which model to apply
- Need to compare multiple model approaches
- Want to optimize forecast accuracy

## Input Data Format
```python
# Required: Time series data
time_series = [100, 105, 110, 115, 120, 125, 130, ...]

# Optional: Data characteristics
data_characteristics = {
    "trend_detected": bool,
    "seasonality_detected": bool,
    "volatility": "low/medium/high",
    "min_value": float,
    "max_value": float,
    "min_span": int,  # minimum forecast span
    "max_span": int,  # maximum forecast span
    "expected_span": int  # expected forecast span
}

# Optional: Model constraints
constraints = {
    "max_order": 5,  # max polynomial order
    "preferred_models": [...],  # preferred model types
    "avoid_models": [...],  # models to avoid
    "must_include_trend": bool,
    "must_include_seasonality": bool
}

# Optional: Scoring criteria
scoring = {
    "primary": "accuracy",  # or "interpretability", "speed", "complexity"
    "weight_accuracy": 0.4,
    "weight_interpretability": 0.3,
    "weight_speed": 0.2,
    "weight_complexity": 0.1
}
```

## Output Format
```python
{
    "recommendation": {
        "primary_model": "Holt's Method",
        "confidence": 0.85,
        "ranked_models": [
            {"model": "Holt's Method", "score": 0.85, "rank": 1},
            {"model": "Linear Regression", "score": 0.78, "rank": 2},
            {"model": "Exponential Trend", "score": 0.65, "rank": 3}
        ]
    },
    "analysis": {
        "detected_patterns": {
            "trend": {"type": "upward", "strength": 0.75, "significance": 0.02},
            "seasonality": {"type": "annual", "strength": 0.45, "significance": 0.08},
            "volatility": "medium",
            "linearity": 0.68
        },
        "model_evaluation": {
            "Holt's Method": {"fit_score": 0.92, "complexity": "low"},
            "Linear Regression": {"fit_score": 0.78, "complexity": "low"},
            "Exponential Trend": {"fit_score": 0.85, "complexity": "medium"}
        }
    },
    "suggested_parameters": {
        "Holt's Method": {"alpha": 0.3, "beta": 0.1},
        "Linear Regression": {},
        "Exponential Trend": {}
    },
    "expected_accuracy": {
        "best_case": 0.85,
        "expected": 0.78,
        "worst_case": 0.65
    }
}
```

## Processing Steps
1. Analyze data patterns (trend, seasonality, volatility, linearity)
2. Evaluate each candidate model against detected patterns
3. Apply scoring criteria (accuracy, complexity, speed, interpretability)
4. Rank models by composite score
5. Generate model-specific parameter recommendations
6. Estimate expected accuracy for top models
7. Provide detailed explanation for recommendations
8. Return structured result

## Example Use Case
```python
# Input: Mixed characteristics data
time_series = [100, 105, 112, 118, 125, 124, 128, 133, 140, 138]

# Expected output:
# - Primary: Holt's Method (trend + some seasonality)
# - Alternatives: Linear Regression, Exponential Trend
# - Parameters: alpha=0.3, beta=0.1 for Holt
```

## Related Skills
- `agent-linear-regression` - First choice for linear patterns
- `agent-holt-method` - First choice for trend patterns
- `agent-statistics-calculation` - For validation

## Dependencies
- All model agents (for pattern matching)
- `numpy`, `scipy` - For statistical analysis

## Analysis Methods
- **Trend detection**: Linear regression R², Mann-Kendall test
- **Seasonality detection**: Autocorrelation, periodogram
- **Volatility analysis**: Rolling variance, coefficient of variation
- **Linearity analysis**: Kurtosis, skewness, linear vs. transformed data fit

## Notes
- Consider domain knowledge when interpreting results
- Higher complexity models may be overkill for simple data
- Balance between fit quality and forecast horizon
