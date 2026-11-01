# Quick Start Guide: ONS Emissions Data Analysis

## Getting Started in 5 Minutes

### 1. Launch Jupyter Notebook

```bash
cd C:\Users\jones\Documents\Coding\Projects\ONS_Data\ONS_Employment
jupyter notebook
```

Then open: `notebooks/exploratory.ipynb`

### 2. Key Data Loading Pattern

```python
import pandas as pd
from pathlib import Path

def load_emissions_sheet(filepath, sheet_name, skiprows=6):
    """Load ONS emissions data with proper formatting."""
    df = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows)
    df = df.rename(columns={df.columns[0]: 'Year'})
    df = df[pd.to_numeric(df['Year'], errors='coerce').notna()].copy()
    df['Year'] = df['Year'].astype(int)
    df = df.set_index('Year')
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Load GHG data
data_dir = Path('../data')
ghg_total = load_emissions_sheet(
    data_dir / 'provisionalatmoshpericemissionsghg.xlsx',
    'GHG total',
    skiprows=6
)
```

### 3. Quick Visualization

```python
import matplotlib.pyplot as plt

# UK total emissions over time
uk_total = ghg_total.sum(axis=1)

plt.figure(figsize=(12, 6))
plt.plot(uk_total.index, uk_total.values, linewidth=2.5)
plt.title('UK Total GHG Emissions (1990-2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Emissions (thousand tonnes CO2e)')
plt.grid(True, alpha=0.3)
plt.show()
```

## File Structure Reference

### Skiprows Guide

| File Type | Skiprows | Example Sheet |
|-----------|----------|---------------|
| GHG | 6 | 'GHG total', 'CO2' |
| Pollutants | 5 | 'PM10', 'PM2.5' |
| Acid Rain | 5 | 'SO2', 'NOx' |
| Intensity | 6 | 'GHG intensity' |

### File Paths

```python
files = {
    'ghg': 'data/provisionalatmoshpericemissionsghg.xlsx',
    'pollutants': 'data/provisionalatmosphericemissionsotherpollutants.xlsx',
    'acid_rain': 'data/provisinalatmosphericemissionsacidrainprecursors.xlsx',
    'ghg_intensity': 'data/provatmosphericemissionsghgintensity.xlsx'
}
```

## Key Sheets by File

### 1. GHG File (10 sheets)
- `GHG total` - All greenhouse gases combined
- `CO2`, `CH4`, `N2O` - Individual gases
- `HFC`, `PFC`, `SF6`, `NF3` - F-gases

### 2. Pollutants File (8 sheets)
- `PM10`, `PM2.5` - Particulate matter
- `CO` - Carbon monoxide
- `NMVOC` - Volatile organic compounds
- `Benzene`, `13BD` - Specific pollutants

### 3. Acid Rain File (6 sheets)
- `Acid Rain Precursor` - Total
- `SO2`, `NOx`, `NH3` - Individual precursors

### 4. Intensity File (5 sheets)
- `GHG intensity` - Emissions per £ million
- `CO2 intensity` - CO2 per £ million

## Common Tasks

### Get UK Total Emissions

```python
uk_total = df.sum(axis=1)  # Sum across all industries
```

### Get Top Industries

```python
latest_year = df.index[-1]
top_10 = df.loc[latest_year].sort_values(ascending=False).head(10)
```

### Calculate Percentage Change

```python
start = df.iloc[0].sum()
end = df.iloc[-1].sum()
pct_change = ((end - start) / start) * 100
print(f"Change: {pct_change:+.1f}%")
```

### Extract Industry Time Series

```python
# For a specific industry (e.g., code 'D' = Electricity supply)
electricity_emissions = df['D']
```

## Troubleshooting

### Issue: File not found
**Solution**: Check you're in the correct directory
```python
import os
print(os.getcwd())  # Should end with ONS_Employment
```

### Issue: Empty DataFrame
**Solution**: Adjust skiprows parameter (try 5 or 6)

### Issue: Year column contains text
**Solution**: The filtering step should remove non-numeric rows:
```python
df = df[pd.to_numeric(df['Year'], errors='coerce').notna()]
```

### Issue: NaN values in data
**Solution**: This is normal - some industries don't produce certain emissions
```python
df.fillna(0)  # If you need zeros instead
# Or
df.dropna(axis=1, how='all')  # Remove columns that are all NaN
```

## Data Units

| Pollutant | Unit |
|-----------|------|
| GHG Total | Thousand tonnes CO2 equivalent |
| CO2 | Thousand tonnes |
| CH4, N2O | Thousand tonnes CO2 equivalent |
| PM10, PM2.5 | Thousand tonnes |
| SO2, NOx | Thousand tonnes SO2 equivalent |
| GHG Intensity | Thousand tonnes CO2e per £ million |

## Example Analysis Workflows

### 1. Time Series Trend Analysis

```python
import numpy as np
from scipy import stats

# Linear trend for UK total
uk_total = df.sum(axis=1)
years = uk_total.index.values
emissions = uk_total.values

slope, intercept, r_value, p_value, std_err = stats.linregress(years, emissions)

print(f"Annual change: {slope:,.0f} kt/year")
print(f"R²: {r_value**2:.3f}")
print(f"p-value: {p_value:.2e}")
```

### 2. Industry Contribution Analysis

```python
# Calculate each industry's share in latest year
latest_year = df.index[-1]
contributions = df.loc[latest_year]
total = contributions.sum()
shares = (contributions / total * 100).sort_values(ascending=False)

print("Top 5 contributors:")
for industry, share in shares.head().items():
    print(f"  {industry}: {share:.1f}%")
```

### 3. Comparison Across Pollutants

```python
# Load multiple pollutants
pollutants = {}
for sheet in ['GHG total', 'CO2', 'CH4']:
    pollutants[sheet] = load_emissions_sheet(files['ghg'], sheet)

# Normalize to 1990 = 100
normalized = {}
for name, data in pollutants.items():
    total = data.sum(axis=1)
    normalized[name] = (total / total.iloc[0]) * 100

# Compare
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
for name, series in normalized.items():
    plt.plot(series.index, series.values, label=name, linewidth=2)
plt.legend()
plt.show()
```

## Next Steps

1. **Explore**: Run `notebooks/exploratory.ipynb` for full analysis
2. **Customize**: Modify plots and analysis for your specific questions
3. **Model**: Move to ML modeling (see `src/models/`)
4. **Document**: Read `DATA_STRUCTURE_SUMMARY.md` for full details

## Resources

- **Full Documentation**: `DATA_STRUCTURE_SUMMARY.md`
- **Exploratory Notebook**: `notebooks/exploratory.ipynb`
- **ONS Source**: https://www.ons.gov.uk/economy/environmentalaccounts
- **Project Instructions**: `CLAUDE.md`

---

**Last Updated**: 2025-10-28
