# Agent: Multi-Regression Model

**Priority:** 8
**Suggested Model:** `qwen-3.5-14b`
**Type:** Model Forecasting Agent

## Description
Handles multi-variable regression forecasting for time series data with multiple predictor variables. This agent applies multiple linear regression to capture relationships between multiple independent variables and a dependent variable.

## When to Use
Use this agent when:
- Multiple factors influence the outcome
- Historical data includes relevant predictor variables
- Need to understand variable impacts on forecast

## Input Data Format
```python
# Required: Multi-dimensional data structure
data = {
    "target": [100, 105, 110, 115, 120],  # Values to forecast
    "predictors": [
        [10, 12, 14, 16, 18],  # Predictor 1 (e.g., temperature)
        [50, 52, 54, 56, 58],  # Predictor 2 (e.g., advertising spend)
        [100, 102, 104, 106, 108]  # Predictor 3 (e.g., inventory)
    ]
}

# Optional: Time series identifier/name
identifier = "multi_factor_forecast"

# Optional: Number of periods to forecast
forecast_periods = 3
```

## Output Format
```python
{
    "model_type": "Multi-Variable Regression",
    "equation": "y = a + b1*x1 + b2*x2 + b3*x3 + ...",
    "parameters": {
        "intercept": float,
        "coefficients": [
            {"variable": "x1", "coefficient": float, "p_value": float, "importance": float},
            {"variable": "x2", "coefficient": float, "p_value": float, "importance": float},
            ...
        ],
        "r_squared": float,
        "adjusted_r_squared": float,
        "f_statistic": float,
        "p_value": float
    },
    "forecasts": [float, float, ...],
    "confidence_intervals": {
        "lower": [float, ...],
        "upper": [float, ...]
    },
    "accuracy_metrics": {
        "mape": float,
        "mae": float,
        "rmse": float,
        "adj_r_squared": float
    },
    "variable_analysis": {
        "significant_variables": [...],
        "correlation_matrix": {...}
    }
}
```

## Processing Steps
1. Validate input data (ensure matching dimensions)
2. Check minimum sample size (at least 2n+1 observations, where n = number of predictors)
3. Apply multiple linear regression: Y = X * B
4. Generate forecasts using predictor values
5. Calculate confidence intervals for forecasts
6. Calculate accuracy metrics and statistical significance
7. Analyze variable importance and correlations
8. Return structured result

## Example Use Case
```python
# Input: Sales forecast with multiple drivers
data = {
    "target": [1000, 1100, 1200, 1300, 1400],
    "predictors": {
        "advertising": [10, 15, 20, 25, 30],
        "seasonality": [0.8, 0.9, 1.0, 0.95, 0.9],
        "economy_index": [100, 102, 104, 106, 108]
    }
}

# Expected output: Multi-factor forecast with variable impacts
# Forecast: ~1500-1600 range
```

## Related Skills
- `agent-statistics-calculation` - For detailed statistical analysis
- `agent-chart-visualization` - For multi-variable plots

## Dependencies
- `multi_regression.py` - Contains multi-variable regression implementation
- `numpy`, `scipy` - For matrix operations and statistics

## Notes
- Requires higher quality and more data than single-variable models
- Be careful of multicollinearity between predictors
- Consider interaction terms if variables may interact
- 14b model recommended for more complex statistical analysis
