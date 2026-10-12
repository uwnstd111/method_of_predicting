# Agent: Linear Regression Model

**Priority:** 1 (Highest)
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles linear regression trend forecasting for time series data. This agent processes raw input data and applies the simple linear trend model to generate forecasts.

## When to Use
Use this agent when:
- Data shows a clear linear trend (straight line pattern)
- Forecasting horizon is short to medium
- Simple, interpretable model is preferred

## Input Data Format
```python
# Required: List of numeric time series values
time_series = [10.5, 12.3, 11.8, 13.1, 14.2, ...]

# Optional: Time series identifier/name
identifier = "sales_data_2024"

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Linear Regression",
    "equation": "y = mx + b",
    "parameters": {
        "slope": float,
        "intercept": float,
        "r_squared": float,
        "correlation": float
    },
    "forecasts": [float, float, ...],
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float
    }
}
```

## Processing Steps
1. Transform time series to linear space (if needed)
2. Calculate linear regression parameters (slope, intercept)
3. Generate forecast values
4. Calculate accuracy metrics (MAPE, MAE, RMSE, R-squared)
5. Return structured result

## Example Use Case
```python
# Input: Monthly sales data showing steady growth
time_series = [100, 105, 110, 115, 120]

# Expected output: Linear projection of sales trend
# Forecast: ~125, 130, 135 for next 3 months
```

## Related Skills
- `agent-statistics-calculation` - For detailed statistical analysis
- `agent-chart-visualization` - For plotting linear trend

## Dependencies
- `exponencial.py` - Contains `linregEXP` function
- `numpy`, `statistics` - For numerical calculations