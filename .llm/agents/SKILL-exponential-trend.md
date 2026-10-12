# Agent: Exponential Trend Model

**Priority:** 4
**Suggested Model:** `qwen-3.5-7b`
**Type:** Model Forecasting Agent

## Description
Handles exponential trend forecasting for time series data showing exponential growth or decay patterns. This agent transforms data to linear space using logarithms and applies linear regression.

## When to Use
Use this agent when:
- Data shows exponential growth or decay (curved upward/downward)
- Rate of change is proportional to current value
- Compounding effects are present (e.g., population, compound interest)

## Input Data Format
```python
# Required: List of numeric time series values (must be positive)
time_series = [10, 20, 40, 80, 160, ...]  # Exponential growth example

# Optional: Time series identifier/name
identifier = "population_growth"

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Exponential Trend",
    "equation": "y = a * b^x",
    "linearized_equation": "ln(y) = ln(a) + ln(b) * x",
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
        "rmse": float,
        "s_y_exp": float
    },
    "trend_analysis": {
        "growth_rate": float,
        "doubling_time": float,  # if growing
        "halving_time": float    # if decaying
    }
}
```

## Processing Steps
1. Validate input data (all values must be positive)
2. Transform data using natural logarithm: ln(y)
3. Apply linear regression to transformed data
4. Transform back to exponential scale: exp(linear_prediction)
5. Generate forecasts for requested periods
6. Calculate accuracy metrics on original scale
7. Calculate growth/decay rate and time constants
8. Return structured result

## Example Use Case
```python
# Input: Exponential growth (e.g., viral spread, compound growth)
time_series = [10, 21, 43, 86, 172, 344]

# Expected output: Exponential projection
# Forecast: ~688, 1376, 2752 (doubling pattern)
```

## Related Skills
- `agent-brown-smoothing` - For stable/flat data
- `agent-holt-method` - For linear trend data

## Dependencies
- `exponencial.py` - Contains:
  - `linregEXP()` - Linear regression
  - `ret_EXP_parameters()` - Parameter extraction
  - `ret_transfromed_exp_model_to_linear()` - Data transformation
  - `ret_coef_of_variation_exp()` - Coefficient of variation
  - `ret_coef_of_determination_exp()` - R-squared calculation
  - `retPointPrognosis_EXP()` - Point prognosis

## Notes
- Watch for data with values near zero (can cause issues with log transformation)
- Consider data scaling if values span many orders of magnitude
