"""
Script to create the exploratory notebook for ONS emissions data analysis.
"""
import nbformat as nbf
from pathlib import Path

# Create a new notebook
nb = nbf.v4.new_notebook()

# Add cells
cells = []

# Title and Introduction
cells.append(nbf.v4.new_markdown_cell("""# UK Atmospheric Emissions Exploratory Analysis

This notebook provides comprehensive exploration and visualization of ONS atmospheric emissions data.

## Data Sources

1. **Greenhouse Gases (GHG)**: Total GHG, CO2, CH4, N2O, HFC, PFC, SF6, NF3
2. **Other Pollutants**: PM10, PM2.5, CO, NMVOC, Benzene, 1,3-Butadiene
3. **Acid Rain Precursors**: Total ARP, SO2, NOx, NH3
4. **GHG Intensity**: Emissions per £ million of economic output

All data spans from 1990 to 2024 (provisional) by industry sector (SIC codes).

## Analysis Structure

1. Data loading and preprocessing
2. Structure exploration
3. Time series visualization
4. Cross-sectional analysis
5. Key insights and patterns"""))

# Cell 1: Imports
cells.append(nbf.v4.new_code_cell("""# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11

# Define color palettes (colorblind-friendly)
COLORS = {
    'primary': '#0173B2',
    'secondary': '#DE8F05',
    'success': '#029E73',
    'danger': '#CC78BC',
    'warning': '#CA9161',
    'info': '#56B4E9'
}

print("Libraries imported successfully")"""))

# Section 1
cells.append(nbf.v4.new_markdown_cell("""## 1. Data Loading Functions

ONS Excel files have a specific structure:
- First 6 rows contain metadata and headers
- Column headers are SIC industry codes (A, B, C, etc.)
- First column contains years (1990-2024)
- Multiple sheets for different pollutants/gases"""))

# Cell 2: File paths
cells.append(nbf.v4.new_code_cell("""# Define file paths
data_dir = Path(r'..\\data')

files = {
    'ghg': data_dir / 'provisionalatmoshpericemissionsghg.xlsx',
    'pollutants': data_dir / 'provisionalatmosphericemissionsotherpollutants.xlsx',
    'acid_rain': data_dir / 'provisinalatmosphericemissionsacidrainprecursors.xlsx',
    'ghg_intensity': data_dir / 'provatmosphericemissionsghgintensity.xlsx'
}

# Verify files exist
for name, path in files.items():
    if path.exists():
        size_mb = path.stat().st_size / (1024 * 1024)
        print(f"✓ {name:15s}: {path.name:60s} ({size_mb:.2f} MB)")
    else:
        print(f"✗ {name:15s}: NOT FOUND")"""))

# Cell 3: Loading functions
cells.append(nbf.v4.new_code_cell("""def load_emissions_sheet(filepath, sheet_name, skiprows=6):
    \"\"\"
    Load an ONS emissions sheet with proper formatting.

    Parameters
    ----------
    filepath : Path
        Path to the Excel file
    sheet_name : str
        Name of the sheet to load
    skiprows : int, default=6
        Number of header rows to skip

    Returns
    -------
    pd.DataFrame
        DataFrame with years as index and industry codes as columns
    \"\"\"
    # Read the sheet
    df = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows)

    # First column contains years (sometimes labeled as 'SIC code')
    df = df.rename(columns={df.columns[0]: 'Year'})

    # Filter to only numeric years
    df = df[pd.to_numeric(df['Year'], errors='coerce').notna()].copy()
    df['Year'] = df['Year'].astype(int)

    # Set year as index
    df = df.set_index('Year')

    # Convert all columns to numeric, replacing errors with NaN
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def get_industry_name_mapping(filepath, sheet_name, skiprows=6):
    \"\"\"
    Extract the mapping between SIC codes and industry names.

    Returns
    -------
    dict
        Mapping of SIC code to industry name
    \"\"\"
    # Read with one less skiprow to get the industry names
    df = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows-1, nrows=1)

    # First column is 'Industry name', rest are industry descriptions
    mapping = {}
    for i, col in enumerate(df.columns[1:]):
        if pd.notna(df.iloc[0, i+1]):
            mapping[col] = str(df.iloc[0, i+1])

    return mapping


print("Data loading functions defined")"""))

# Section 2
cells.append(nbf.v4.new_markdown_cell("""## 2. Load Greenhouse Gas (GHG) Data

The GHG file contains multiple greenhouse gases measured in thousand tonnes of CO2 equivalent."""))

# Cell 4: Load GHG
cells.append(nbf.v4.new_code_cell("""# Load GHG sheets
ghg_sheets = ['GHG total', 'CO2', 'CH4', 'N2O', 'HFC', 'PFC', 'SF6', 'NF3']
ghg_data = {}

print("Loading GHG data...")
for sheet in ghg_sheets:
    try:
        ghg_data[sheet] = load_emissions_sheet(files['ghg'], sheet)
        print(f"  ✓ {sheet:15s}: {ghg_data[sheet].shape[0]} years × {ghg_data[sheet].shape[1]} industries")
    except Exception as e:
        print(f"  ✗ {sheet:15s}: Error - {str(e)[:50]}")

# Get industry mapping
industry_names = get_industry_name_mapping(files['ghg'], 'GHG total')
print(f"\\nIndustry sectors: {len(industry_names)}")"""))

# Cell 5: Display mapping
cells.append(nbf.v4.new_code_cell("""# Display industry mapping
print("\\nSIC Code to Industry Name Mapping:")
print("=" * 80)
for code, name in list(industry_names.items())[:15]:  # Show first 15
    print(f"{code:5s}: {name[:70]}")
if len(industry_names) > 15:
    print(f"... and {len(industry_names) - 15} more industries")"""))

# Cell 6: Examine data
cells.append(nbf.v4.new_code_cell("""# Examine GHG total data structure
print("\\nGHG Total Data Sample:")
print("=" * 80)
print(ghg_data['GHG total'].iloc[:5, :8])  # First 5 years, 8 industries
print("\\nData coverage:")
print(f"  Years: {ghg_data['GHG total'].index.min()} to {ghg_data['GHG total'].index.max()}")
print(f"  Industries: {ghg_data['GHG total'].shape[1]}")
print(f"  Missing values: {ghg_data['GHG total'].isna().sum().sum()} ({100*ghg_data['GHG total'].isna().sum().sum()/(ghg_data['GHG total'].shape[0]*ghg_data['GHG total'].shape[1]):.1f}%)")"""))

# Section 3
cells.append(nbf.v4.new_markdown_cell("""## 3. Load Other Pollutants Data

Includes particulate matter (PM10, PM2.5), carbon monoxide (CO), and volatile organic compounds."""))

# Cell 7: Load pollutants
cells.append(nbf.v4.new_code_cell("""# Load pollutant sheets
pollutant_sheets = ['PM10', 'PM2.5', 'CO', 'NMVOC', 'Benzene', '13BD']
pollutant_data = {}

print("Loading pollutant data...")
for sheet in pollutant_sheets:
    try:
        pollutant_data[sheet] = load_emissions_sheet(files['pollutants'], sheet, skiprows=5)
        print(f"  ✓ {sheet:15s}: {pollutant_data[sheet].shape[0]} years × {pollutant_data[sheet].shape[1]} industries")
    except Exception as e:
        print(f"  ✗ {sheet:15s}: Error - {str(e)[:50]}")"""))

# Section 4
cells.append(nbf.v4.new_markdown_cell("""## 4. Load Acid Rain Precursor Data

Sulfur dioxide (SO2), nitrogen oxides (NOx), and ammonia (NH3) contribute to acid rain."""))

# Cell 8: Load acid rain
cells.append(nbf.v4.new_code_cell("""# Load acid rain sheets
acid_rain_sheets = ['Acid Rain Precursor', 'SO2', 'NOx', 'NH3']
acid_rain_data = {}

print("Loading acid rain precursor data...")
for sheet in acid_rain_sheets:
    try:
        acid_rain_data[sheet] = load_emissions_sheet(files['acid_rain'], sheet, skiprows=5)
        print(f"  ✓ {sheet:20s}: {acid_rain_data[sheet].shape[0]} years × {acid_rain_data[sheet].shape[1]} industries")
    except Exception as e:
        print(f"  ✗ {sheet:20s}: Error - {str(e)[:50]}")"""))

# Section 5
cells.append(nbf.v4.new_markdown_cell("""## 5. Load GHG Intensity Data

Emissions intensity measures emissions per unit of economic output (£ million)."""))

# Cell 9: Load intensity
cells.append(nbf.v4.new_code_cell("""# Load intensity sheets
intensity_sheets = ['GHG intensity', 'CO2 intensity']
intensity_data = {}

print("Loading GHG intensity data...")
for sheet in intensity_sheets:
    try:
        intensity_data[sheet] = load_emissions_sheet(files['ghg_intensity'], sheet)
        print(f"  ✓ {sheet:20s}: {intensity_data[sheet].shape[0]} years × {intensity_data[sheet].shape[1]} industries")
    except Exception as e:
        print(f"  ✗ {sheet:20s}: Error - {str(e)[:50]}")"""))

# Section 6
cells.append(nbf.v4.new_markdown_cell("""## 6. Time Series Visualization: Total UK Emissions

Let's visualize the overall trends for different emission types across the UK."""))

# Cell 10: Calculate totals
cells.append(nbf.v4.new_code_cell("""# Calculate total UK emissions by summing across all industries

def get_total_emissions(df):
    \"\"\"Sum emissions across all industry columns to get UK total.\"\"\"
    return df.sum(axis=1, skipna=True)

# Calculate totals for key pollutants
uk_totals = pd.DataFrame({
    'GHG Total': get_total_emissions(ghg_data['GHG total']),
    'CO2': get_total_emissions(ghg_data['CO2']),
    'CH4': get_total_emissions(ghg_data['CH4']),
    'N2O': get_total_emissions(ghg_data['N2O']),
})

print("UK Total Emissions (first 5 years):")
print(uk_totals.head())"""))

# Cell 11: GHG plots
cells.append(nbf.v4.new_code_cell("""# Plot 1: Greenhouse Gas Trends
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('UK Greenhouse Gas Emissions Trends (1990-2024)', fontsize=16, fontweight='bold')

# GHG Total
axes[0, 0].plot(uk_totals.index, uk_totals['GHG Total'], linewidth=2.5, color=COLORS['primary'])
axes[0, 0].set_title('Total GHG Emissions', fontsize=13, fontweight='bold')
axes[0, 0].set_ylabel('Thousand tonnes CO2 equiv.', fontsize=11)
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].axhline(y=uk_totals['GHG Total'].mean(), color='red', linestyle='--', alpha=0.5, label='Mean')
axes[0, 0].legend()

# CO2
axes[0, 1].plot(uk_totals.index, uk_totals['CO2'], linewidth=2.5, color=COLORS['secondary'])
axes[0, 1].set_title('Carbon Dioxide (CO2) Emissions', fontsize=13, fontweight='bold')
axes[0, 1].set_ylabel('Thousand tonnes', fontsize=11)
axes[0, 1].grid(True, alpha=0.3)

# CH4
axes[1, 0].plot(uk_totals.index, uk_totals['CH4'], linewidth=2.5, color=COLORS['success'])
axes[1, 0].set_title('Methane (CH4) Emissions', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Year', fontsize=11)
axes[1, 0].set_ylabel('Thousand tonnes CO2 equiv.', fontsize=11)
axes[1, 0].grid(True, alpha=0.3)

# N2O
axes[1, 1].plot(uk_totals.index, uk_totals['N2O'], linewidth=2.5, color=COLORS['danger'])
axes[1, 1].set_title('Nitrous Oxide (N2O) Emissions', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('Year', fontsize=11)
axes[1, 1].set_ylabel('Thousand tonnes CO2 equiv.', fontsize=11)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Calculate percentage changes
print("\\nPercentage change from 1990 to 2024:")
for col in uk_totals.columns:
    start = uk_totals[col].iloc[0]
    end = uk_totals[col].iloc[-1]
    pct_change = ((end - start) / start) * 100
    print(f"  {col:15s}: {pct_change:+.1f}%")"""))

# Cell 12: Pollutant plots
cells.append(nbf.v4.new_code_cell("""# Plot 2: Other Pollutants
pollutant_totals = pd.DataFrame({
    'PM10': get_total_emissions(pollutant_data['PM10']),
    'PM2.5': get_total_emissions(pollutant_data['PM2.5']),
    'CO': get_total_emissions(pollutant_data['CO']),
    'NMVOC': get_total_emissions(pollutant_data['NMVOC']),
})

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('UK Air Pollutant Emissions Trends (1990-2024)', fontsize=16, fontweight='bold')

pollutants = ['PM10', 'PM2.5', 'CO', 'NMVOC']
colors = [COLORS['primary'], COLORS['secondary'], COLORS['success'], COLORS['danger']]

for i, (pollutant, color) in enumerate(zip(pollutants, colors)):
    ax = axes[i//2, i%2]
    ax.plot(pollutant_totals.index, pollutant_totals[pollutant], linewidth=2.5, color=color)
    ax.set_title(f'{pollutant} Emissions', fontsize=13, fontweight='bold')
    ax.set_ylabel('Thousand tonnes', fontsize=11)
    ax.grid(True, alpha=0.3)
    if i >= 2:
        ax.set_xlabel('Year', fontsize=11)

plt.tight_layout()
plt.show()

print("\\nPercentage change from 1990 to 2024:")
for col in pollutant_totals.columns:
    start = pollutant_totals[col].iloc[0]
    end = pollutant_totals[col].iloc[-1]
    pct_change = ((end - start) / start) * 100
    print(f"  {col:10s}: {pct_change:+.1f}%")"""))

# Cell 13: Acid rain plots
cells.append(nbf.v4.new_code_cell("""# Plot 3: Acid Rain Precursors
acid_totals = pd.DataFrame({
    'Total ARP': get_total_emissions(acid_rain_data['Acid Rain Precursor']),
    'SO2': get_total_emissions(acid_rain_data['SO2']),
    'NOx': get_total_emissions(acid_rain_data['NOx']),
    'NH3': get_total_emissions(acid_rain_data['NH3']),
})

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('UK Acid Rain Precursor Emissions (1990-2024)', fontsize=16, fontweight='bold')

precursors = ['Total ARP', 'SO2', 'NOx', 'NH3']
colors = [COLORS['primary'], COLORS['secondary'], COLORS['success'], COLORS['warning']]

for i, (precursor, color) in enumerate(zip(precursors, colors)):
    ax = axes[i//2, i%2]
    ax.plot(acid_totals.index, acid_totals[precursor], linewidth=2.5, color=color)
    ax.set_title(f'{precursor} Emissions', fontsize=13, fontweight='bold')
    ax.set_ylabel('Thousand tonnes SO2 equiv.', fontsize=11)
    ax.grid(True, alpha=0.3)
    if i >= 2:
        ax.set_xlabel('Year', fontsize=11)

plt.tight_layout()
plt.show()

print("\\nPercentage change from 1990 to 2024:")
for col in acid_totals.columns:
    start = acid_totals[col].iloc[0]
    end = acid_totals[col].iloc[-1]
    pct_change = ((end - start) / start) * 100
    print(f"  {col:12s}: {pct_change:+.1f}%")"""))

# Section 7
cells.append(nbf.v4.new_markdown_cell("""## 7. Interactive Plotly Visualizations

Interactive charts allow for detailed exploration of the data."""))

# Cell 14: Plotly interactive
cells.append(nbf.v4.new_code_cell("""# Create interactive plot for GHG components
fig = go.Figure()

ghg_components = ['CO2', 'CH4', 'N2O']
for component in ghg_components:
    fig.add_trace(go.Scatter(
        x=uk_totals.index,
        y=uk_totals[component],
        mode='lines+markers',
        name=component,
        line=dict(width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{fullData.name}</b><br>Year: %{x}<br>Emissions: %{y:,.0f} kt<extra></extra>'
    ))

fig.update_layout(
    title='<b>UK Greenhouse Gas Components (1990-2024)</b>',
    xaxis_title='Year',
    yaxis_title='Emissions (thousand tonnes CO2 equiv.)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)')
)

fig.show()"""))

# Section 8
cells.append(nbf.v4.new_markdown_cell("""## 8. Industry-Specific Analysis

Examine emissions by industry sector to identify major contributors."""))

# Cell 15: Top industries
cells.append(nbf.v4.new_code_cell("""# Get the latest year's emissions by industry for GHG
latest_year = ghg_data['GHG total'].index[-1]
latest_emissions = ghg_data['GHG total'].loc[latest_year].sort_values(ascending=False)

print(f"Top 15 Industries by GHG Emissions in {latest_year}:")
print("=" * 80)
for i, (code, value) in enumerate(latest_emissions.head(15).items(), 1):
    industry_name = industry_names.get(code, code)
    print(f"{i:2d}. {code:5s} - {industry_name[:50]:50s}: {value:>10,.0f} kt CO2e")"""))

# Cell 16: Industry bar plot
cells.append(nbf.v4.new_code_cell("""# Plot top 10 industries
top_industries = latest_emissions.head(10)

fig = go.Figure()

fig.add_trace(go.Bar(
    y=[industry_names.get(code, code)[:40] for code in top_industries.index],
    x=top_industries.values,
    orientation='h',
    marker=dict(color=COLORS['primary']),
    text=[f"{v:,.0f}" for v in top_industries.values],
    textposition='auto',
))

fig.update_layout(
    title=f'<b>Top 10 Industries by GHG Emissions ({latest_year})</b>',
    xaxis_title='Emissions (thousand tonnes CO2 equiv.)',
    yaxis_title='',
    height=600,
    template='plotly_white',
    font=dict(size=11),
    yaxis=dict(autorange='reversed')  # Highest at top
)

fig.show()"""))

# Cell 17: Time series for top industries
cells.append(nbf.v4.new_code_cell("""# Time series for top 5 industries
top_5_codes = latest_emissions.head(5).index

fig = go.Figure()

for code in top_5_codes:
    industry_name = industry_names.get(code, code)[:30]
    fig.add_trace(go.Scatter(
        x=ghg_data['GHG total'].index,
        y=ghg_data['GHG total'][code],
        mode='lines+markers',
        name=f"{code}: {industry_name}",
        line=dict(width=2.5),
        marker=dict(size=5)
    ))

fig.update_layout(
    title='<b>Top 5 Industries: GHG Emissions Over Time</b>',
    xaxis_title='Year',
    yaxis_title='Emissions (thousand tonnes CO2 equiv.)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=11),
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.9)')
)

fig.show()"""))

# Section 9
cells.append(nbf.v4.new_markdown_cell("""## 9. Summary Statistics and Key Insights"""))

# Cell 18: Summary
cells.append(nbf.v4.new_code_cell("""print("=" * 80)
print("UK ATMOSPHERIC EMISSIONS: KEY FINDINGS (1990-2024)")
print("=" * 80)

print("\\n1. GREENHOUSE GASES")
print("-" * 80)
for gas in ['GHG Total', 'CO2', 'CH4', 'N2O']:
    start = uk_totals[gas].iloc[0]
    end = uk_totals[gas].iloc[-1]
    pct_change = ((end - start) / start) * 100
    direction = "decreased" if pct_change < 0 else "increased"
    print(f"  {gas:12s}: {start:>10,.0f} → {end:>10,.0f} kt CO2e ({pct_change:+.1f}%, {direction})")

print("\\n2. AIR POLLUTANTS")
print("-" * 80)
for pollutant in ['PM10', 'PM2.5', 'CO', 'NMVOC']:
    start = pollutant_totals[pollutant].iloc[0]
    end = pollutant_totals[pollutant].iloc[-1]
    pct_change = ((end - start) / start) * 100
    direction = "decreased" if pct_change < 0 else "increased"
    print(f"  {pollutant:8s}: {start:>10,.0f} → {end:>10,.0f} kt ({pct_change:+.1f}%, {direction})")

print("\\n3. ACID RAIN PRECURSORS")
print("-" * 80)
for precursor in ['Total ARP', 'SO2', 'NOx', 'NH3']:
    start = acid_totals[precursor].iloc[0]
    end = acid_totals[precursor].iloc[-1]
    pct_change = ((end - start) / start) * 100
    direction = "decreased" if pct_change < 0 else "increased"
    print(f"  {precursor:12s}: {start:>10,.0f} → {end:>10,.0f} kt SO2e ({pct_change:+.1f}%, {direction})")

print("\\n4. TOP CONTRIBUTING INDUSTRIES (2024)")
print("-" * 80)
for i, (code, value) in enumerate(latest_emissions.head(5).items(), 1):
    industry_name = industry_names.get(code, code)[:50]
    pct_of_total = (value / latest_emissions.sum()) * 100
    print(f"  {i}. {code} - {industry_name[:40]:40s}: {pct_of_total:5.1f}% of total")

print("\\n" + "=" * 80)"""))

# Conclusion
cells.append(nbf.v4.new_markdown_cell("""## Conclusion

This exploratory analysis reveals several key patterns in UK atmospheric emissions:

1. **Overall Decline**: Most emission types show significant reductions from 1990-2024, with particularly strong decreases in acid rain precursors (SO2, NOx) and traditional air pollutants (PM10, PM2.5).

2. **GHG Trends**: While total GHG emissions have decreased, the rate of reduction varies by gas type. CO2 remains the dominant contributor.

3. **Industry Patterns**: A small number of industry sectors account for the majority of emissions, suggesting targeted intervention opportunities.

4. **Data Quality**: 2024 figures are provisional and subject to revision. Some industry breakdowns may have suppressed values for disclosure control.

### Next Steps for ML Analysis:

- **Forecasting**: Use LSTM/transformer models to predict future emission trajectories
- **Classification**: Identify industry sectors with similar emission patterns
- **Anomaly Detection**: Detect unusual emission events or trends
- **Causal Analysis**: Investigate relationships between economic indicators and emissions
- **Policy Impact**: Model the effects of different intervention scenarios"""))

# Add all cells to notebook
nb['cells'] = cells

# Write notebook
output_path = Path(r"C:\Users\jones\Documents\Coding\Projects\ONS_Data\ONS_Employment\notebooks\exploratory.ipynb")
with open(output_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook created successfully: {output_path}")
print(f"Total cells: {len(cells)}")
print("Cell breakdown:")
print(f"  - Markdown cells: {sum(1 for c in cells if c['cell_type'] == 'markdown')}")
print(f"  - Code cells: {sum(1 for c in cells if c['cell_type'] == 'code')}")
