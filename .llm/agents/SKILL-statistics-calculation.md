# Agent: Statistics Calculation

**Priority:** 11
**Suggested Model:** `qwen-3.5-7b`
**Type:** Analysis/Validation Agent

## Description
Computes accuracy metrics, detailed statistics, and performance analysis for chosen forecasting models. This agent validates and evaluates the results of any forecasting model.

## When to Use
Use this agent when:
- Need detailed statistical validation
- Comparing multiple model outputs
- Preparing reports for stakeholders
- Debugging model performance

## Input Data Format
```python
# Required: Actual vs. Forecast data
actual_values = [100, 105, 110, 115, 120]
forecast_values = [102, 107, 112, 118, 123]

# Optional: Time series context
time_series = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

# Optional: Model type (for context)
model_type = "Holt's Method"

# Optional: Confidence level for intervals
confidence_level = 0.95  # Default: 0.95

# Optional: Additional statistics
additional_stats = {
    "include_decomposition": True,
    "include_residuals": True,
    "include_forecast_errors": True
}
```

## Output Format
```python
{
    "fit_metrics": {
        "mape": 0.0234,  # Mean Absolute Percentage Error (2.34%)
        "mae": 2.34,     # Mean Absolute Error
        "rmse": 3.21,    # Root Mean Square Error
        "mse": 10.3,     # Mean Square Error
        "mape_trend": "decreasing",  # trend in errors
        "bias": 0.12     # forecast bias
    },
    "confidence": {
        "lower_95": [...],
        "upper_95": [...],
        "confidence_level": 0.95
    },
    "model_performance": {
        "r_squared": 0.92,
        "adjusted_r_squared": 0.91,
        "correlation": 0.96,
        "information_criteria": {
            "aic": 123.4,
            "bic": 145.6,
            "aicc": 127.8
        }
    },
    "residual_analysis": {
        "mean": 0,
        "std": 3.21,
        "autocorrelation": [...],
        "normality_test": {
            "test": "jarque_bera",
            "p_value": 0.08,
            "significant": False
        }
    },
    "statistical_significance": {
        "f_test_p_value": 0.001,
        "coefficients_significant": [True, False, True],
        "t_tests": [...]
    },
    "robustness": {
        "outlier_influence": "low",
        "sensitivity_analysis": {
            "alpha_sensitivity": "low",
            "beta_sensitivity": "medium"
        }
    }
}
```

## Processing Steps
1. Align actual vs. forecast values
2. Calculate fit metrics (MAPE, MAE, RMSE, MSE)
3. Calculate confidence intervals for forecasts
4. Compute model performance metrics (R², correlation, AIC/BIC)
5. Analyze residuals (mean, std, autocorrelation, normality)
6. Perform statistical significance tests
7. Assess robustness and sensitivity
8. Return structured result

## Example Use Case
```python
# Input: Actual sales vs. forecast from Holt's method
actual_values = [100, 105, 110, 115, 120]
forecast_values = [102, 107, 112, 118, 123]
model_type = "Holt's Method"

# Expected output:
# - MAPE: ~3.1%
# - RMSE: ~2.5
# - R²: ~0.98
# - 95% CI for next period: [125, 129]
```

## Related Skills
- `agent-auto-model-selection` - For model recommendation
- `agent-chart-visualization` - For plotting statistics

## Dependencies
- `numpy`, `scipy.stats` - For statistical tests
- `statistics` - For basic statistics

## Key Metrics Explained
- **MAPE**: Mean Absolute Percentage Error (easiest to interpret)
- **MAE**: Mean Absolute Error (less sensitive to outliers)
- **RMSE**: Root Mean Square Error (penalizes large errors)
- **R²**: Coefficient of Determination (model fit quality)
- **AIC/BIC**: Information criteria (model selection, lower = better)
- **Confidence Intervals**: Range where true value likely falls

## Notes
- MAPE can be unstable with values near zero
- RMSE and MAE behave differently with outliers
- Consider using weighted metrics for importance differences
- Always report confidence intervals with point forecasts
