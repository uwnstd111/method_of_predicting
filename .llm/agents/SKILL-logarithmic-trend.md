# Agent: Logarithmic Trend Model

**Priority:** 6
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles logarithmic trend forecasting for time series data showing logarithmic growth/decay patterns (y = a + b * ln(x)). This agent applies linear regression to log-transformed time index.

## When to Use
Use this agent when:
- Data shows rapid initial change that slows down over time
- Diminishing returns pattern exists
- Saturation behavior is observed (e.g., learning curves, adoption curves)

## Input Data Format
```python
# Required: List of numeric time series values
time_series = [100, 90, 85, 82, 81, 80.5, ...]  # Diminishing growth example

# Optional: Time series identifier/name
identifier = "learning_curve"

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Logarithmic Trend",
    "equation": "y = a + b * ln(x)",
    "parameters": {
        "a": float,  # Asymptote
        "b": float,
        "r_squared": float,
        "correlation": float,
        "asymptote": float
    },
    "forecasts": [float, float, ...],
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float
    },
    "saturation_analysis": {
        "asymptotic_level": float,
        "approach_rate": float,
        "saturation_percentage": float
    }
}
```

## Processing Steps
1. Validate input data (non-zero, non-negative values)
2. Transform time index using natural logarithm: ln(x)
3. Apply linear regression: ln(y) = a + b * ln(x)
4. Transform back to original scale
5. Generate forecasts for requested periods
6. Calculate accuracy metrics
7. Analyze asymptotic behavior and saturation
8. Return structured result

## Example Use Case
```python
# Input: Learning curve (rapid improvement, then slowing)
time_series = [50, 45, 42, 40, 39, 38.5, 38.3]

# Expected output: Logarithmic approach to asymptote
# Forecast: ~38.1, ~38.05, ~38.02 (approaching ~38)
```

## Related Skills
- `agent-exponential-trend` - For exponential patterns
- `agent-polynomial-trend` - For more complex curves

## Dependencies
- `logarythmical.py` - Contains logarithmic trend implementation
- `numpy` - For numerical operations

## Notes
- Good for modeling adoption, learning, or saturation phenomena
- Less useful for long-term forecasting (asymptotic behavior)
