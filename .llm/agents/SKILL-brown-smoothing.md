# Agent: Brown Smoothing Model

**Priority:** 2
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles Brown's Single Exponential Smoothing for time series forecasting. This agent applies simple exponential smoothing with a single smoothing constant (alpha).

## When to Use
Use this agent when:
- Data shows no clear trend or seasonality
- Data is relatively stable with random fluctuations
- Need a simple, baseline forecasting model

## Input Data Format
```python
# Required: List of numeric time series values
time_series = [10.5, 12.3, 11.8, 13.1, 14.2, ...]

# Optional: Time series identifier/name
identifier = "sales_data_2024"

# Optional: Smoothing constant (alpha, 0 < alpha < 1)
# Default: 0.3
alpha = 0.3

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Brown Smoothing",
    "parameters": {
        "alpha": float,
        "smoothing_constant": float
    },
    "forecast": float,
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float,
        "mse": float
    },
    "model_performance": {
        "is_stable": bool,
        "confidence_level": float
    }
}
```

## Processing Steps
1. Validate input data (minimum 2-3 observations required)
2. Initialize forecast with first data point
3. Apply exponential smoothing formula: F(t+1) = alpha * A(t) + (1-alpha) * F(t)
4. Generate forecasts for requested periods
5. Calculate accuracy metrics using historical fit
6. Return structured result

## Example Use Case
```python
# Input: Stable sales data without trend
time_series = [100, 102, 98, 101, 99, 100]

# Expected output: Smoothed forecast around mean value
# Forecast: ~99-101 range
```

## Related Skills
- `agent-holt-method` - For data with trend component
- `agent-statistics-calculation` - For detailed statistical analysis

## Dependencies
- `brown.py` - Contains Brown's smoothing implementation
- `numpy` - For numerical operations