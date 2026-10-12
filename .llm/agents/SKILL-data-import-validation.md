# Agent: Data Import/Validation

**Priority:** 9
**Suggested Model:** `qwen-3.5-3b`
**Type:** Utility/Data Processing Agent

## Description
Handles file import, CSV parsing, data validation, and preprocessing for time series forecasting. This agent manages the initial data ingestion and quality checks.

## When to Use
Use this agent when:
- Importing data from various file formats
- Data requires cleaning or validation
- Preparing data for analysis pipeline

## Input Data Format
```python
# Required: File path or raw data
input_source = "/path/to/file.csv"  # or {"raw_data": [...], "format": "csv"}

# Optional: File format
file_format = "csv"  # or "excel", "json", "txt"

# Optional: Column specifications
columns = {
    "target_column": "values",
    "time_column": "date",
    "additional_columns": ["col1", "col2"]
}

# Optional: Validation parameters
validation = {
    "min_rows": 10,
    "max_missing": 0.1,  # 10% max missing
    "min_value": 0,
    "max_value": 1000
}

# Optional: Encoding (for text files)
encoding = "utf-8"
```

## Output Format
```python
{
    "import_status": "success/failed",
    "file_info": {
        "path": str,
        "format": str,
        "rows_read": int,
        "columns_read": [str, ...]
    },
    "data_info": {
        "target_values": [...],
        "target_count": int,
        "min": float,
        "max": float,
        "mean": float,
        "std": float
    },
    "validation_results": {
        "passed": bool,
        "missing_percentage": float,
        "outliers_detected": int,
        "null_values": {
            "column": {int, float, ...}
        }
    },
    "preprocessed_data": {
        "time_series": [...],
        "metadata": {...}
    }
}
```

## Processing Steps
1. Read file based on specified format
2. Parse columns according to specifications
3. Validate data structure and types
4. Check for missing values, outliers, and domain violations
5. Perform basic preprocessing (handle missing values, normalize if needed)
6. Extract target time series
7. Generate data statistics
8. Return structured result

## Example Use Case
```python
# Input: CSV file with sales data
input_source = "sales_data_2024.csv"
columns = {"target_column": "sales", "time_column": "month"}
validation = {"min_rows": 12, "max_missing": 0.05}

# Expected output: Validated and preprocessed time series
# Ready for use in forecasting models
```

## Related Skills
- `agent-auto-model-selection` - After validation, select appropriate model
- `agent-statistics-calculation` - For detailed analysis

## Dependencies
- `pandas` - For data manipulation
- `numpy` - For numerical operations

## Common Issues
- **Encoding problems**: Specify correct encoding for text files
- **Date parsing**: May need to specify date format
- **Missing values**: Decide on imputation strategy
- **Outliers**: Consider transformation or robust methods
