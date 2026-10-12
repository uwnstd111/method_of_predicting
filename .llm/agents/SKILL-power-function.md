# Agent: Power Function Model

**Priority:** 5
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles power function trend forecasting for time series data following a power law relationship (y = a * x^b). This agent transforms data using logarithms and applies linear regression.

## When to Use
Use this agent when:
- Data follows a power law relationship
- Log-log plot shows linear pattern
- Scale-invariant relationships exist (e.g., fractal patterns, some physical laws)

## Input Data Format
```python
# Required: List of numeric time series values (must be positive)
time_series = [10, 100, 1000, 10000, ...]

# Optional: Time series identifier/name
identifier = "fractal_pattern"

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Power Function",
    "equation": "y = a * x^b",
    "linearized_equation": "ln(y) = ln(a) + b * ln(x)",
    "parameters": {
        "a": float,
        "b": float,
        "ln_a": float,
        "ln_b": float,
        "r_squared": float,
        "correlation": float
    },
    "forecasts": [float, float, ...],
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float
    },
    "scale_analysis": {
        "elasticity": float,
        "scale_factor": float
    }
}
```

## Processing Steps
1. Validate input data (all values must be positive, no zeros)
2. Transform data: ln(y) = ln(a) + b * ln(x)
3. Apply linear regression to transformed data
4. Transform back to power scale: exp(linear_prediction)
5. Generate forecasts for requested periods
6. Calculate accuracy metrics
7. Calculate elasticity and scale factors
8. Return structured result

## Example Use Case
```python
# Input: Power law relationship (e.g., area vs. length squared)
time_series = [10, 20, 40, 80, 160]  # Area ~ length^2

# Expected output: Power law projection
# Forecast: ~320, 640, 1280
```

## Related Skills
- `agent-exponential-trend` - For exponential relationships
- `agent-logarithmic-trend` - For logarithmic relationships

## Dependencies
- Similar to exponential trend (uses logarithmic transformation)
- `numpy` - For numerical operations

## Notes
- More general than exponential (handles both growth and decay)
- Useful for physical, biological, and economic systems with scale-invariant properties
