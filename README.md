Here is a detailed `README.md` for your project:

# Battery Cycling Data Analysis

This project provides tools for processing and visualizing battery cycling data from various sources. The main functionality includes importing data, processing it, and generating combined capacity plots.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/battery-cycling-data-analysis.git
    cd battery-cycling-data-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Importing Data

The `import_data` module provides functions to import data from different sources:

- `process_eclab_mpr(mpr_file_path, theoretical_capacity)`
- `process_neware_data(ndax_file_path, theoretical_capacity)`

### Plotting Data

The `plot_combined_capacity` function generates a combined capacity plot from multiple dataframes:

```python
import import_data
import numpy as np
import matplotlib.pyplot as plt

def plot_combined_capacity(dataframes, labels, min_cycle=None, max_cycle=None, styles=None, save_image=False, save_path='combined_cap.png'):
    # Function implementation
```

### Example

```python
import import_data

df1 = import_data.process_eclab_mpr('path/to/eclab_file.mpr', theoretical_capacity=1.5)
df2 = import_data.process_neware_data('path/to/neware_file.ndax', theoretical_capacity=0.52)

plot_combined_capacity([df1, df2], ['Label1', 'Label2'], min_cycle=1, max_cycle=250, save_image=True, save_path='combined_cap.png')
```

## Functions

### `import_data`

- **`process_eclab_mpr(mpr_file_path, theoretical_capacity)`**: Processes ECLab MPR files.
- **`process_neware_data(ndax_file_path, theoretical_capacity)`**: Processes Neware NDAX files.

### `main.py`

- **`plot_combined_capacity(dataframes, labels, min_cycle=None, max_cycle=None, styles=None, save_image=False, save_path='combined_cap.png')`**: Plots combined capacity data from multiple dataframes.

## Examples

### Processing ECLab Data

```python
import import_data

df = import_data.process_eclab_mpr('path/to/eclab_file.mpr', theoretical_capacity=1.5)
print(df.head())
```

### Processing Neware Data

```python
import import_data

df = import_data.process_neware_data('path/to/neware_file.ndax', theoretical_capacity=0.52)
print(df.head())
```

### Plotting Combined Capacity

```python
import import_data
import matplotlib.pyplot as plt

df1 = import_data.process_eclab_mpr('path/to/eclab_file.mpr', theoretical_capacity=1.5)
df2 = import_data.process_neware_data('path/to/neware_file.ndax', theoretical_capacity=0.52)

fig = plot_combined_capacity([df1, df2], ['Label1', 'Label2'], min_cycle=1, max_cycle=250, save_image=True, save_path='combined_cap.png')
plt.show()
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.