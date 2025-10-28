# ONS Employment Analysis

A data science and machine learning project for analyzing ONS (Office for National Statistics) employment data using PyTorch for deep learning and scikit-learn for traditional machine learning approaches.

## Features

- Deep learning models using PyTorch
- Traditional ML algorithms using scikit-learn
- Comprehensive data analysis and visualization
- Jupyter notebook-based exploratory analysis
- Support for XGBoost and LightGBM gradient boosting

## Project Structure

```
ONS_Employment/
├── data/                  # Data files (not tracked in git)
├── notebooks/             # Jupyter notebooks for analysis
├── scripts/               # Python scripts
├── src/                   # Source code
├── tests/                 # Unit tests
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