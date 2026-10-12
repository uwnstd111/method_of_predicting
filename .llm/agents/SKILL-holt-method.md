# Agent: Holt's Method (Double Exponential Smoothing)

**Priority:** 3
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles Holt's Double Exponential Smoothing for time series with trend component. This agent applies two smoothing constants (alpha for level, beta for trend) to capture both level and trend in the data.

## When to Use
Use this agent when:
- Data shows a clear trend (upward or downward)
- No seasonality is present
- Need to capture trend component in forecasting

## Input Data Format
```python
# Required: List of numeric time series values
time_series = [10.5, 12.3, 11.8, 13.1, 14.2, ...]

# Optional: Time series identifier/name
identifier = "sales_data_2024"

# Optional: Smoothing constants
# Default: alpha=0.3, beta=0.1
alpha = 0.3
beta = 0.1

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Holt's Method (Double Exponential Smoothing)",
    "parameters": {
        "alpha": float,
        "beta": float,
        "level": float,
        "trend": float
    },
    "forecasts": [float, float, ...],
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float,
        "mse": float
    },
    "trend_analysis": {
        "trend_direction": "up/down/stable",
        "trend_strength": float
    }
}
```

## Processing Steps
1. Validate input data (minimum 4-5 observations recommended)
2. Initialize level and trend components
3. Apply double exponential smoothing:
   - Level: L(t) = alpha * A(t) + (1-alpha) * (L(t-1) + T(t-1))
   - Trend: T(t) = beta * (L(t) - L(t-1)) + (1-beta) * T(t-1)
4. Generate forecasts: F(t+m) = L(t) + m * T(t)
5. Calculate accuracy metrics
6. Analyze trend direction and strength
7. Return structured result

## Example Use Case
```python
# Input: Sales data with clear upward trend
time_series = [100, 110, 122, 135, 149, 164]

# Expected output: Trend-adjusted forecast
# Forecast: ~180, 194, 209 (continuing upward trend)
```

## Related Skills
- `agent-brown-smoothing` - For data without trend
- `agent-exponential-trend` - For exponential growth patterns

## Dependencies
- `holt.py` - Contains Holt's method implementation
- `numpy` - For numerical operations