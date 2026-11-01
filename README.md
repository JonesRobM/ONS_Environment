# ONS Environmental Emissions Analysis

A comprehensive data science and machine learning project for analyzing and interpreting UK atmospheric emissions and environmental pollutant data from ONS (Office for National Statistics). This project combines exploratory data analysis, statistical methods, and machine learning techniques to understand environmental trends, patterns, and impacts.

## Features

- **Environmental Data Analysis**: Comprehensive analysis of 4 ONS atmospheric emissions datasets
- **Exploratory Analysis**: Interactive Jupyter notebooks for data exploration and visualization
- **Machine Learning**: Both shallow learning (scikit-learn, XGBoost, LightGBM) and deep learning (PyTorch) approaches
- **Time Series Analysis**: Forecasting and trend analysis for emissions data
- **Educational Examples**: Well-documented tutorials demonstrating analytical techniques
- **Visualization**: Publication-quality plots and interactive dashboards

## Datasets

The project analyzes four ONS atmospheric emissions datasets:

1. **Greenhouse Gas (GHG) Emissions** (8.4MB)
   - CO2, methane, nitrous oxide, fluorinated gases
   - Sector-specific emissions data

2. **Other Atmospheric Pollutants** (6.4MB)
   - Particulate matter, VOCs, heavy metals
   - Persistent organic pollutants

3. **Acid Rain Precursors** (4.3MB)
   - SO2, NOx, NH3 emissions
   - Agricultural, industrial, and transport sectors

4. **GHG Emissions Intensity** (2.1MB)
   - Emissions per unit of economic activity
   - Efficiency and decarbonization metrics

## Project Structure

```
ONS_Employment/
├── data/                  # Environmental emissions datasets (not tracked in git)
│   ├── provisionalatmoshpericemissionsghg.xlsx
│   ├── provisionalatmosphericemissionsotherpollutants.xlsx
│   ├── provisinalatmosphericemissionsacidrainprecursors.xlsx
│   └── provatmosphericemissionsghgintensity.xlsx
├── notebooks/             # Jupyter notebooks for exploratory analysis
├── scripts/               # Python scripts for data processing and analysis
├── src/                   # Source code modules
│   ├── data/              # Data loading and preprocessing
│   ├── models/            # ML models (shallow and deep learning)
│   ├── utils/             # Utility functions
│   └── visualization/     # Plotting and visualization tools
├── tests/                 # Unit tests
├── .claude/               # Claude Code configuration and agents
├── pyproject.toml         # Project configuration
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip or uv package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ONS_Employment
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

**Option A: Using pip**
```bash
pip install -e .
```

**Option B: Using requirements.txt**
```bash
pip install -r requirements.txt
```

**Option C: With development dependencies**
```bash
pip install -e ".[dev]"
```

### GPU Support

For GPU-accelerated PyTorch, install the CUDA version:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Usage

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory to access analysis notebooks.

### Running Scripts

```bash
python scripts/your_script.py
```

## Development

### Installing Development Dependencies

```bash
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

This project uses Black and Ruff for code formatting and linting:

```bash
black .
ruff check .
```

### Type Checking

```bash
mypy src/
```

## Dependencies

### Core Libraries
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **SciPy**: Scientific computing

### Machine Learning
- **PyTorch**: Deep learning framework
- **scikit-learn**: Traditional ML algorithms
- **XGBoost**: Gradient boosting
- **LightGBM**: Gradient boosting

### Visualization
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive plots

### Additional Tools
- **Jupyter**: Interactive notebooks
- **tqdm**: Progress bars
- **pydantic**: Data validation

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.