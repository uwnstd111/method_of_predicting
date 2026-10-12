# Quick Start Guide: Qwen3.5 Agent Configuration

## Overview

This configuration sets up 12 specialized agents for the `method_of_predicting` project using Qwen3.5 models. Each agent has a specific skill (`SKILL.md`) file and recommended model size.

## Fast Setup

### 1. Download Models

Create a `.llm/models/` directory and download Qwen3.5 model files.

**Recommended minimal setup:**
```
.llm/models/
├── qwen-3.5-7b/          # For 6 model agents (forecasting)
├── qwen-3.5-14b/         # For 2 model agents (complex tasks)
└── qwen-3.5-3b/          # For 2 utility agents (optional, use 7b)
```

**Minimal setup (3 models only):**
```
.llm/models/
├── qwen-3.5-7b/          # All model agents
└── qwen-3.5-14b/         # Auto-selection & multi-regression
```

### 2. Map Models

Update `.llm/models.txt` if using custom paths:
```
# Edit this file for your specific model locations
qwen-3.5-0.5b:~/.llm/models/qwen-3.5-0.5b:0
qwen-3.5-7b:~/.llm/models/qwen-3.5-7b:0
qwen-3.5-14b:~/.llm/models/qwen-3.5-14b:0
```

### 3. Load Configuration

```python
import yaml
from pathlib import Path

config = yaml.safe_load(
    Path(".llm/config.yaml").read_text()
)
```

## Agent Quick Reference

### Standard Forecasting Workflow

```
Data → Import Agent → Select Agent → Model Agent → Stats Agent → Chart Agent
```

```python
# Minimal workflow
from zed import spawn_agent

# 1. Import & validate data
data_agent = spawn_agent(
    label="Load data",
    message=f"Import: {csv_path}",
    model="qwen-3.5-7b"
)

# 2. Auto-select best model
select_agent = spawn_agent(
    label="Select model",
    message=f"Analyze: {data_agent.wait()}",
    model="qwen-3.5-14b"
)

# 3. Run recommended model
model_agent = spawn_agent(
    label="Forecast",
    message=f"Apply: {select_agent.wait()}",
    model="qwen-3.5-7b"
)

# 4. Calculate stats
stats_agent = spawn_agent(
    label="Validate",
    message=f"Check: {model_agent.wait()}",
    model="qwen-3.5-7b"
)
```

### Direct Model Usage (Skip Auto-Selection)

```python
# Linear regression
linear_agent = spawn_agent(
    label="Linear trend",
    message="Apply linear regression",
    model="qwen-3.5-7b"
)

# Holt's method (good for trend data)
holt_agent = spawn_agent(
    label="Holt's smoothing",
    message="Apply double exponential smoothing",
    model="qwen-3.5-7b"
)

# Exponential trend (good for growth/decay)
exp_agent = spawn_agent(
    label="Exponential trend",
    message="Apply exponential transformation",
    model="qwen-3.5-7b"
)
```

## Model Selection Guide

| Task | Recommended Model | Agent |
|------|-------------------|-------|
| Quick linear forecast | qwen-3.5-7b | `agent-linear-regression` |
| Trend data | qwen-3.5-7b | `agent-holt-method` |
| Exponential growth | qwen-3.5-7b | `agent-exponential-trend` |
| Complex analysis | qwen-3.5-14b | `agent-auto-model-selection` |
| Multi-variable | qwen-3.5-14b | `agent-multi-regression` |
| Data validation | qwen-3.5-7b | `agent-data-import-validation` |
| Charts | qwen-3.5-3b | `agent-chart-visualization` |

## File Locations

```
.method_of_predicting-master/
├── .llm/
│   ├── config.yaml           # Master configuration
│   ├── models.txt            # Model mappings
│   ├── agents/
│   │   ├── SKILL-*.md        # 12 skill definitions
│   │   └── skills.txt        # Skill registry
│   └── models/               # Model files (download here)
└── [existing project files]
```

## Testing the Setup

```python
# Quick test
from zed import spawn_agent

# Test agent spawn
test_agent = spawn_agent(
    label="Test connection",
    message="Check Qwen3.5 model availability",
    model="qwen-3.5-7b"
)

result = test_agent.wait()
print(f"Agent ready: {result}")
```

## Common Use Cases

### Case 1: New Time Series

```python
# Given: CSV file with sales data
csv_path = "sales_data.csv"

# Load and analyze
data_agent = spawn_agent(
    label="Analyze new data",
    message=f"Import and validate: {csv_path}",
    model="qwen-3.5-7b"
)

# Auto-select model
select_agent = spawn_agent(
    label="Choose best model",
    message=f"Analyze patterns: {data_agent.wait()}",
    model="qwen-3.5-14b"
)

# Apply model
forecast = select_agent.wait()
```

### Case 2: Quick Trend Forecast

```python
# Given: Time series showing upward trend
ts = [100, 105, 112, 120, 130]

# Use Holt's method directly
holt_agent = spawn_agent(
    label="Trend forecast",
    message=f"Apply Holt's to: {ts}",
    model="qwen-3.5-7b"
)

result = holt_agent.wait()
print(f"Forecast: {result['forecasts']}")
```

### Case 3: Multi-Factor Forecast

```python
# Given: Sales data with multiple drivers
data = {
    "target": [100, 105, 110, 115],
    "advertising": [10, 12, 14, 16],
    "seasonality": [0.8, 0.9, 1.0, 0.95]
}

# Use multi-regression
multi_agent = spawn_agent(
    label="Multi-factor forecast",
    message=f"Analyze: {data}",
    model="qwen-3.5-14b"
)

result = multi_agent.wait()
print(f"Model: {result['parameters']['equation']}")
```

## Performance Tips

1. **Cache model results**: Similar data can reuse model weights
2. **Use lighter models**: 3b-7b for simple tasks, save 14b for complex analysis
3. **Parallelize**: Run independent agents simultaneously
4. **Batch imports**: Process similar files together

## Troubleshooting

**Agent fails to spawn:**
- Check model files exist at configured paths
- Verify `models.txt` has correct entries
- Test with smallest model first (0.5b or 1.5b)

**Poor forecast accuracy:**
- Re-run `agent-auto-model-selection`
- Check data quality with `agent-data-import-validation`
- Review residuals with `agent-statistics-calculation`

**Slow performance:**
- Use 3b or 7b model instead of 14b
- Reduce model complexity (lower polynomial order, etc.)
- Enable result caching

## Next Steps

1. Download Qwen3.5 models
2. Configure `.llm/models.txt`
3. Test agent spawning
4. Integrate with PyQt5 GUI
5. Add custom models if needed

## Support

- Check `config.yaml` for detailed agent specifications
- Review `SKILL-*.md` files for specific use cases
- Use `agent-auto-model-selection` when unsure
