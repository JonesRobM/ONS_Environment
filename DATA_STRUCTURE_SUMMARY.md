# ONS Atmospheric Emissions Data Structure Summary

## Overview

This document provides a comprehensive summary of the ONS atmospheric emissions Excel files analyzed for the UK climate emissions project.

**Analysis Date**: 2025-10-28
**Data Coverage**: 1990-2024 (2024 figures are provisional)

---

## File Inventory

| File Name | Size | Sheets | Description |
|-----------|------|--------|-------------|
| `provisionalatmoshpericemissionsghg.xlsx` | 8.32 MB | 10 | Greenhouse gas emissions |
| `provisionalatmosphericemissionsotherpollutants.xlsx` | 6.35 MB | 8 | Air pollutants (PM, CO, VOCs) |
| `provisinalatmosphericemissionsacidrainprecursors.xlsx` | 4.23 MB | 6 | Acid rain precursors |
| `provatmosphericemissionsghgintensity.xlsx` | 2.10 MB | 5 | Emissions intensity metrics |

**Total Data**: ~21 MB across 29 sheets

---

## 1. Greenhouse Gases File

**File**: `provisionalatmoshpericemissionsghg.xlsx`

### Sheets Available

1. **Table_of_contents** - Navigation sheet
2. **Notes** - Methodology and caveats
3. **GHG total** - Total greenhouse gas emissions (CO2 equivalent)
4. **CO2** - Carbon dioxide emissions
5. **CH4** - Methane emissions (CO2e)
6. **N2O** - Nitrous oxide emissions (CO2e)
7. **HFC** - Hydrofluorocarbons (CO2e)
8. **PFC** - Perfluorocarbons (CO2e)
9. **SF6** - Sulfur hexafluoride (CO2e)
10. **NF3** - Nitrogen trifluoride (CO2e)

### Data Structure

- **Format**: Wide format with years as rows, industry SIC codes as columns
- **Skiprows**: 6 (header metadata)
- **Time Range**: 1990-2024 (35 years)
- **Industries**: ~135-159 industry codes (varies by sheet)
- **Units**: Thousand tonnes (CO2 or CO2 equivalent)
- **Basis**: UK residence basis (territorial emissions)

### Key Characteristics

- First 6 rows contain metadata, notes, and multi-level headers
- Row 1 (after skiprows=6) contains industry names
- Row 2+ contain SIC codes as column headers (A, B, C, D, etc.)
- Years in first column, numeric data in remaining columns
- Some cells marked as `[low]` for non-zero but negligible values
- Total figures calculated from raw data (may not match sum of displayed figures)

---

## 2. Other Pollutants File

**File**: `provisionalatmosphericemissionsotherpollutants.xlsx`

### Sheets Available

1. **Table_of_contents** - Navigation
2. **Notes** - Methodology notes
3. **PM10** - Particulate matter (≤10 μm)
4. **PM2.5** - Particulate matter (≤2.5 μm)
5. **CO** - Carbon monoxide
6. **NMVOC** - Non-methane volatile organic compounds
7. **Benzene** - Benzene emissions
8. **13BD** - 1,3-Butadiene emissions

### Data Structure

- **Format**: Wide format (same as GHG file)
- **Skiprows**: 5 (one fewer than GHG sheets)
- **Time Range**: 1990-2024
- **Industries**: ~162 industry codes
- **Units**: Thousand tonnes
- **Basis**: UK residence basis

### Key Characteristics

- Similar structure to GHG file but with 5 header rows instead of 6
- Includes natural world emissions for some pollutants
- PM data particularly relevant for air quality analysis
- Benzene and 1,3-BD are trace pollutants but important for health impacts

---

## 3. Acid Rain Precursors File

**File**: `provisinalatmosphericemissionsacidrainprecursors.xlsx`

### Sheets Available

1. **Table_of_contents** - Navigation
2. **Notes** - Methodology
3. **Acid Rain Precursor** - Total ARP (SO2 equivalent)
4. **SO2** - Sulfur dioxide emissions
5. **NOx** - Nitrogen oxides (SO2 equivalent)
6. **NH3** - Ammonia (SO2 equivalent)

### Data Structure

- **Format**: Wide format
- **Skiprows**: 5
- **Time Range**: 1990-2024
- **Industries**: ~162 industry codes
- **Units**: Thousand tonnes (SO2 or SO2 equivalent)
- **Basis**: UK residence basis

### Key Characteristics

- ARP total calculated as SO2 equivalent for comparability
- NOx values need conversion factor (÷ 0.6957) to get nitrogen oxide units
- Strong declining trend expected due to environmental regulations
- Key for understanding acidification and eutrophication impacts

---

## 4. GHG Intensity File

**File**: `provatmosphericemissionsghgintensity.xlsx`

### Sheets Available

1. **Table_of_contents** - Navigation
2. **Notes** - Methodology (extensive notes on economic output calculation)
3. **GHG intensity** - GHG per £ million output
4. **CO2 intensity** - CO2 per £ million output
5. **CO2 intensity SDG basis** - CO2 intensity for Sustainable Development Goal reporting

### Data Structure

- **Format**: Wide format
- **Skiprows**: 6
- **Time Range**: 1990-2024
- **Industries**: ~136 industry codes
- **Units**: Thousand tonnes CO2e per £ million
- **Basis**: UK residence basis, divided by economic output

### Key Characteristics

- Intensity metrics control for economic growth
- Allows comparison of environmental efficiency across time and sectors
- Economic output from ONS national accounts (chained volume measures)
- SDG sheet uses different methodology aligned with UN reporting
- Essential for decoupling analysis (emissions vs economic growth)

---

## Common Data Structure Patterns

### Standard Sheet Layout

```
Row 1-6 (before skiprows): Metadata, titles, notes
Row 1 (after skiprows=6): Industry names (full text)
Row 2 (after skiprows=6): SIC codes (A, B, C, D, E, F, G, etc.)
Row 3+: Years (1990-2024) in first column, emissions data in subsequent columns
```

### SIC Code Structure

- **Single letter codes**: Major industry sections (A = Agriculture, B = Mining, etc.)
- **Multi-character codes**: More granular industry groups (e.g., 01 = Crop production)
- **Special codes**:
  - Total/All industries aggregates
  - Natural world (for some pollutants)
  - Households
  - Extra-territorial organizations

### Data Quality Indicators

- `[low]` - Low but non-zero value
- `NaN` / blank - Missing or suppressed data (disclosure control)
- Provisional figures for latest year (2024)
- Figures subject to revision (especially recent years)

---

## Industry Classification

### Major SIC Sections (Examples)

| Code | Industry Section |
|------|------------------|
| A | Agriculture, forestry and fishing |
| B | Mining and quarrying |
| C | Manufacturing |
| D | Electricity, gas, steam and air conditioning supply |
| E | Water supply; sewerage, waste management |
| F | Construction |
| G | Wholesale and retail trade; repair of motor vehicles |
| H | Transportation and storage |
| I | Accommodation and food service activities |
| J | Information and communication |

*Note*: Full mapping of 135-162 industry codes available via `get_industry_name_mapping()` function.

---

## Time Series Characteristics

### Temporal Coverage

- **Start Year**: 1990 (baseline year for international climate agreements)
- **End Year**: 2024 (provisional)
- **Frequency**: Annual
- **Years**: 35 data points per series

### Expected Trends

1. **GHG Emissions**: Generally declining due to:
   - Shift from coal to gas and renewables
   - Energy efficiency improvements
   - Deindustrialization
   - Climate policy interventions

2. **Air Pollutants**: Strong declines expected due to:
   - Clean Air Acts
   - Vehicle emission standards (Euro 1-6)
   - Industrial regulation

3. **Acid Rain Precursors**: Dramatic reductions from:
   - Desulfurization of power stations
   - Catalytic converters
   - Fuel quality standards

4. **Intensity Metrics**: Should decline faster than absolute emissions due to economic growth

### Structural Breaks to Consider

- **1990**: Baseline year
- **1997-1998**: Dash for gas (coal to gas switching in power generation)
- **2008-2009**: Financial crisis (economic contraction)
- **2020**: COVID-19 pandemic (major disruption)
- **2024**: Provisional data (subject to revision)

---

## Data Loading Recommendations

### Optimal Loading Parameters

```python
# For GHG sheets
ghg_data = pd.read_excel(filepath, sheet_name='GHG total', skiprows=6)

# For pollutant and acid rain sheets
pollutant_data = pd.read_excel(filepath, sheet_name='PM10', skiprows=5)

# For intensity sheets
intensity_data = pd.read_excel(filepath, sheet_name='GHG intensity', skiprows=6)
```

### Post-Processing Steps

1. Rename first column to 'Year'
2. Filter to numeric years only
3. Convert year column to integer
4. Set year as index
5. Convert all other columns to numeric (coerce errors to NaN)
6. Handle `[low]` markers appropriately

### Industry Name Extraction

Industry names are in the row immediately before SIC codes:
```python
# Read with skiprows-1 and nrows=1 to get industry names
names_df = pd.read_excel(filepath, sheet_name=sheet, skiprows=5, nrows=1)
```

---

## Missing Data Patterns

### Types of Missingness

1. **Structural Missingness**: Industries that don't produce certain emissions
2. **Disclosure Control**: Small values suppressed to prevent identification
3. **Measurement Issues**: Some sectors difficult to measure (e.g., natural emissions)
4. **Recent Years**: More likely to have provisional/missing data

### Handling Strategies

- **Time series analysis**: Forward/backward fill may be appropriate for small gaps
- **Cross-sectional analysis**: Consider only complete cases
- **Aggregation**: Summing across industries naturally handles NaN (skip)
- **Imputation**: Use with caution - document methodology

---

## Key Variables for Analysis

### Primary Response Variables

1. **GHG Total** - Overall climate impact
2. **CO2** - Largest GHG component (~80-90%)
3. **CH4** - Important non-CO2 GHG (agriculture, waste)
4. **N2O** - Long-lived GHG (agriculture, industry)
5. **PM2.5** - Health-critical air pollutant
6. **SO2** - Acid rain and health impacts
7. **NOx** - Air quality and eutrophication
8. **GHG Intensity** - Efficiency metric

### Aggregation Options

- **UK Total**: Sum across all industries
- **Sector Totals**: Sum within major SIC sections (A, B, C, etc.)
- **Top Contributors**: Focus on highest-emitting industries
- **Economic Sectors**: Group by economic activity type

---

## Visualization Recommendations

### Time Series Plots

- **Line charts**: Annual trends (1990-2024)
- **Area charts**: Stacked by industry or gas type
- **Small multiples**: Compare multiple pollutants
- **Percent change**: Index to 1990=100 for comparability

### Cross-Sectional Analysis

- **Bar charts**: Top industries (horizontal bars work well)
- **Treemaps**: Hierarchical industry structure
- **Heatmaps**: Industry × year matrix for pattern detection

### Advanced Visualizations

- **Interactive plots**: Plotly for exploration
- **Faceted grids**: Compare multiple pollutants/sectors
- **Decomposition**: Trend, seasonal (if sub-annual), residual
- **Forecast plots**: Show predictions with confidence intervals

### Publication Quality

- Use colorblind-friendly palettes (e.g., Tol, ColorBrewer)
- Clear axis labels with units
- Source attribution (ONS, 2024)
- Highlight provisional data
- Add reference lines (e.g., 1990 baseline, policy targets)

---

## ML Analysis Opportunities

### Shallow Learning Applications

**Dataset Size**: 35 years × 135-162 industries = 4,725+ observations per pollutant

1. **Linear Regression**: Trend analysis, intensity drivers
2. **Random Forest**: Feature importance for emission drivers
3. **k-means Clustering**: Identify similar industry emission profiles
4. **PCA**: Dimensionality reduction for correlated pollutants

### Deep Learning Applications

1. **LSTMs**: Time series forecasting with multiple features
2. **Transformers**: Multi-step ahead predictions
3. **Autoencoders**: Anomaly detection in emission patterns
4. **Graph Neural Networks**: Industry interdependencies

### Feature Engineering Ideas

- Lagged emissions (t-1, t-2, etc.)
- Rolling averages (3-year, 5-year)
- Year-over-year changes
- Cumulative emissions
- Intensity ratios
- Cross-pollutant ratios (e.g., NOx/SO2)
- Industry group aggregates
- Policy indicators (as external features)

---

## Data Quality Notes

### Strengths

- Long time series (35 years)
- Consistent methodology (generally)
- Comprehensive industry coverage
- Official government statistics (high quality)
- International standards (UNFCCC, IPCC guidelines)

### Limitations

- Annual frequency only (no sub-annual variation)
- Provisional latest year
- Some missing/suppressed values
- Industry classification changes over time (SIC revisions)
- Measurement uncertainty (especially CH4, N2O)
- Natural emissions uncertain for some pollutants

### Validation Checks

1. **Consistency**: Total should equal sum of industries (approximately)
2. **Trends**: Check against known policy changes
3. **Outliers**: Investigate unusual year-over-year changes
4. **Comparison**: Cross-check with other ONS series (e.g., energy statistics)

---

## Cleaned Data Output

### CSV Files Generated

1. **notebooks/cleaned_emissions_tidy.csv** (existing)
   - Long format: Year, Industry, Value, Sheet
   - Suitable for ggplot-style plotting

2. **notebooks/uk_emissions_timeseries.csv** (to be generated)
   - Wide format: Year as index, pollutants as columns
   - UK totals across all industries
   - Ready for time series modeling

### Recommended Additional Exports

- **industry_timeseries.csv**: All industries × all years for one pollutant
- **cross_sectional_2024.csv**: Latest year snapshot across industries
- **intensity_metrics.csv**: All intensity measures
- **metadata.json**: Industry code mappings, units, notes

---

## Next Steps for Analysis

### Immediate Priorities

1. ✓ Exploratory notebook created (`notebooks/exploratory.ipynb`)
2. Run notebook to generate visualizations
3. Export cleaned time series data
4. Identify data quality issues

### Short-term Analysis

1. **Trend Analysis**: Quantify emission reductions by pollutant/sector
2. **Breakpoint Detection**: Identify structural changes in trends
3. **Decomposition**: Separate trend, cycle, and irregular components
4. **Correlation Analysis**: Relationships between pollutants

### ML Modeling Roadmap

1. **Baselines**: Simple linear models and naive forecasts
2. **Traditional ML**: Random forests for feature importance
3. **Time Series**: ARIMA, Prophet for forecasting
4. **Deep Learning**: LSTM for multi-step predictions
5. **Ensemble**: Combine multiple approaches

### Documentation Needs

- Data dictionary (full industry code mapping)
- Methodology notes summary
- Code documentation (data loading functions)
- Analysis notebooks (one per analysis type)
- Final report summarizing findings

---

## Contact and References

### Data Source

- **Provider**: Office for National Statistics (ONS)
- **Contact**: Environment.Accounts@ons.gov.uk
- **Series**: UK Environmental Accounts: Air Emissions
- **License**: Open Government Licence v3.0

### Relevant Standards

- UNFCCC reporting guidelines
- IPCC emissions inventory guidance
- UK Standard Industrial Classification (SIC 2007)
- Environmental Accounts framework (SEEA)

### Related Datasets

Consider linking with:
- ONS Energy consumption data
- ONS Economic output (GVA) by industry
- UK Climate Change Act targets
- Air quality monitoring data (DEFRA)
- International comparisons (Eurostat, OECD)

---

*Document created: 2025-10-28*
*For project: ONS_Employment (UK Climate Emissions Analysis)*
*Notebook: notebooks/exploratory.ipynb*
