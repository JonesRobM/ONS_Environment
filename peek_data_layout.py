"""
Script to peek at the actual data layout in the sheets to understand row/column structure.
"""
import pandas as pd
from pathlib import Path

data_dir = Path(r"C:\Users\jones\Documents\Coding\Projects\ONS_Data\ONS_Employment\data")
ghg_file = data_dir / "provisionalatmoshpericemissionsghg.xlsx"

# Read the GHG total sheet with different skiprows to find the actual data
print("=" * 80)
print("EXAMINING DATA LAYOUT - GHG total sheet")
print("=" * 80)

for skip in [0, 3, 4, 5, 6]:
    print(f"\n--- Skip {skip} rows ---")
    df = pd.read_excel(ghg_file, sheet_name="GHG total", skiprows=skip, nrows=10)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns[:8])}")
    print("\nFirst 5 rows:")
    print(df.iloc[:5, :8])
    print()

# Also check a pollutant file
pollutant_file = data_dir / "provisionalatmosphericemissionsotherpollutants.xlsx"
print("\n" + "=" * 80)
print("EXAMINING DATA LAYOUT - PM10 sheet")
print("=" * 80)

for skip in [0, 3, 4, 5]:
    print(f"\n--- Skip {skip} rows ---")
    df = pd.read_excel(pollutant_file, sheet_name="PM10", skiprows=skip, nrows=10)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns[:8])}")
    print("\nFirst 5 rows:")
    print(df.iloc[:5, :8])
    print()
