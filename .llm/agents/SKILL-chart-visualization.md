# Agent: Chart/Visualization

**Priority:** 12
**Suggested Model:** `qwen-3.5-3b`
**Type:** Utility/Visualization Agent

## Description
Prepares data and specifications for chart rendering and visualization in the PyQt5 interface. This agent formats data for plotting and handles visualization specifications.

## When to Use
Use this agent when:
- Preparing data for chart display
- Formatting visualization output
- Creating report figures

## Input Data Format
```python
# Required: Data to visualize
chart_data = {
    "x_values": [...],  # Time index or x-axis values
    "y_values": [...],  # Primary y-axis data
    "type": "line"      # or "scatter", "bar", "area", etc.
}

# Optional: Secondary data (e.g., forecast, confidence intervals)
secondary_data = {
    "forecast": [...],
    "confidence_interval": {
        "lower": [...],
        "upper": [...]
    }
}

# Optional: Chart specifications
specifications = {
    "title": "Sales Forecast",
    "x_label": "Time Period",
    "y_label": "Sales (units)",
    "show_forecast": True,
    "show_confidence": True,
    "show_actual": True,
    "legend_position": "best",
    "grid": True,
    "dpi": 100
}

# Optional: Styling
styling = {
    "primary_color": "#0072CE",
    "forecast_color": "#E7E9EB",
    "actual_color": "#24292E",
    "line_width": 2,
    "marker_size": 5
}
```

## Output Format
```python
{
    "chart_specifications": {
        "chart_type": "Line",
        "title": "Sales Forecast",
        "x_label": "Time Period",
        "y_label": "Sales (units)",
        "figure_size": (10, 6),
        "dpi": 100,
        "layout": {
            "tight_layout": True,
            "pad": 0.05
        }
    },
    "plot_data": {
        "actual": {
            "x": [...],
            "y": [...],
            "label": "Actual",
            "color": "#24292E",
            "style": "solid",
            "linewidth": 2,
            "marker": "o"
        },
        "forecast": {
            "x": [...],
            "y": [...],
            "label": "Forecast",
            "color": "#E7E9EB",
            "style": "dashed",
            "linewidth": 2,
            "marker": "s"
        },
        "confidence_interval": {
            "x": [...],
            "y_upper": [...],
            "y_lower": [...],
            "label": "95% Confidence Interval",
            "color": "#0072CE",
            "style": "dotted",
            "linewidth": 1
        }
    },
    "annotations": [
        {
            "type": "text",
            "x": 0.95,
            "y": 0.95,
            "text": "R² = 0.95",
            "color": "#24292E",
            "fontsize": 10
        }
    ],
    "export_options": {
        "formats": ["png", "svg", "pdf"],
        "default_format": "png",
        "default_dpi": 100
    }
}
```

## Processing Steps
1. Parse and validate chart data
2. Determine optimal chart type based on data characteristics
3. Format primary and secondary data for plotting
4. Apply styling specifications (colors, line styles, markers)
5. Set up annotations and labels
6. Configure export options
7. Return structured result for PyQt5/PyQtGraph rendering

## Example Use Case
```python
# Input: Forecast with confidence intervals
chart_data = {
    "x_values": [1, 2, 3, 4, 5],
    "y_values": [100, 105, 110, 115, 120],
    "type": "line"
}
secondary_data = {
    "forecast": [125, 130, 135, 140],
    "confidence_interval": {
        "lower": [120, 124, 128, 132],
        "upper": [130, 136, 142, 148]
    }
}
specifications = {
    "title": "Sales Forecast",
    "show_forecast": True,
    "show_confidence": True,
    "show_actual": True
}

# Expected output: Structured data for PyQt5 chart widget
# Ready for display in main window
```

## Related Skills
- `agent-linear-regression` - For simple trend charts
- `agent-multi-regression` - For multi-variable plots

## Dependencies
- `pyqt5`, `pyqtgraph` - For chart rendering
- `numpy` - For data formatting

## Chart Types
- **Line**: Time series data (default)
- **Scatter**: Discrete observations
- **Bar**: Categorical comparison
- **Area**: Highlighted regions
- **Dual-axis**: Two y-axes with different scales

## PyQt5 Integration
The output is designed to work with PyQt5's QChart/QGraphics or PySide6 widgets:
```python
# Example integration
def create_chart(chart_spec):
    fig = FigureWidget()
    ax = fig.mpl_axes()
    for dataset in chart_spec["plot_data"].values():
        ax.plot(dataset["x"], dataset["y"], **dataset)
    # ... additional configuration
    return fig
```

## Notes
- Keep file sizes reasonable for GUI display
- Consider interactive vs. static charts
- Ensure accessibility (color-blind friendly palettes)
- Match UI theme colors when possible
