# Agent: Polynomial Trend Model

**Priority:** 7
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles polynomial trend forecasting for time series data following polynomial patterns (y = a + bx + cx² + ...). This agent applies polynomial regression of specified order.

## When to Use
Use this agent when:
- Data shows curved patterns (parabolic, cubic, etc.)
- Linear models don't capture the trend
- Polynomial patterns are theoretically justified

## Input Data Format
```python
# Required: List of numeric time series values
time_series = [10, 15, 24, 37, 54, 75, 100]  # Cubic example

# Optional: Time series identifier/name
identifier = "cubic_pattern"

# Optional: Polynomial order (2-6 recommended)
# Default: 2 (quadratic)
polynomial_order = 3

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Polynomial Trend",
    "equation": "y = a + bx + cx² + ...",
    "order": int,
    "parameters": {
        "coefficients": [float, float, float, ...],
        "r_squared": float,
        "correlation": float
    },
    "forecasts": [float, float, ...],
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float
    },
    "polynomial_analysis": {
        "dominant_term": str,
        "end_behavior": "up/down/stable",
        "inflection_points": [float, ...]
    },
    "overfitting_risk": "low/medium/high"
}
```

## Processing Steps
1. Validate input data and polynomial order
2. Construct polynomial basis functions
3. Apply polynomial regression using least squares
4. Generate forecasts for requested periods
5. Calculate accuracy metrics
6. Analyze polynomial behavior (inflection points, end behavior)
7. Assess overfitting risk (higher orders = higher risk)
8. Return structured result

## Example Use Case
```python
# Input: Cubic pattern (e.g., seasonal with acceleration)
time_series = [10, 25, 50, 85, 130, 185, 250]

# Expected output: Polynomial projection (order 2-3)
# Forecast: ~325, ~410, ~505 (accelerating)
```

## Related Skills
- `agent-exponential-trend` - For exponential patterns
- `agent-multi-regression` - For multi-variable polynomial

## Dependencies
- `polynomial.py` - Contains polynomial trend implementation
- `numpy` - For polynomial operations
- `scipy` - For polynomial fitting (optional)

## Notes
- Higher orders fit data better but increase overfitting risk
- Order 2-3 is usually sufficient for most time series
- Watch for oscillations in forecasts at extreme values
