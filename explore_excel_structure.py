"""
Quick script to explore the structure of ONS atmospheric emissions Excel files.
This will help understand the data before creating the full exploratory notebook.
"""
import pandas as pd
from pathlib import Path

# Define file paths
data_dir = Path(r"C:\Users\jones\Documents\Coding\Projects\ONS_Data\ONS_Employment\data")

files = {
    "GHG": data_dir / "provisionalatmoshpericemissionsghg.xlsx",
    "Other Pollutants": data_dir / "provisionalatmosphericemissionsotherpollutants.xlsx",
    "Acid Rain": data_dir / "provisinalatmosphericemissionsacidrainprecursors.xlsx",
    "GHG Intensity": data_dir / "provatmosphericemissionsghgintensity.xlsx"
}

print("=" * 80)
print("ONS ATMOSPHERIC EMISSIONS DATA STRUCTURE EXPLORATION")
print("=" * 80)

for name, filepath in files.items():
    print(f"\n{'=' * 80}")
    print(f"FILE: {name}")
    print(f"Path: {filepath.name}")
    print(f"Size: {filepath.stat().st_size / (1024*1024):.2f} MB")
    print(f"{'=' * 80}")

    try:
        # Load Excel file
        xl_file = pd.ExcelFile(filepath)

        print(f"\nNumber of sheets: {len(xl_file.sheet_names)}")
        print(f"Sheet names: {xl_file.sheet_names}")

        # Examine each sheet
        for sheet_name in xl_file.sheet_names[:5]:  # Limit to first 5 sheets
            print(f"\n  Sheet: '{sheet_name}'")
            print(f"  {'-' * 70}")

            try:
                # Read sheet
                df = pd.read_excel(filepath, sheet_name=sheet_name, nrows=20)

                print(f"  Shape: {df.shape}")
                print(f"  Columns: {list(df.columns[:10])}")  # First 10 columns

                # Check for year/time columns
                year_cols = [col for col in df.columns if any(x in str(col).lower() for x in ['year', 'date', 'time', '199', '200', '201', '202'])]
                if year_cols:
                    print(f"  Potential time columns: {year_cols[:5]}")

                # Show first few rows
                print(f"\n  First 3 rows:")
                print(df.head(3).to_string(max_cols=8, max_colwidth=30))

            except Exception as e:
                print(f"  Error reading sheet: {str(e)[:100]}")

        if len(xl_file.sheet_names) > 5:
            print(f"\n  ... and {len(xl_file.sheet_names) - 5} more sheets")

    except Exception as e:
        print(f"ERROR: Could not read file: {str(e)}")

print("\n" + "=" * 80)
print("EXPLORATION COMPLETE")
print("=" * 80)
