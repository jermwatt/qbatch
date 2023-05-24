[![Python application](https://github.com/jermwatt/quickbatch/actions/workflows/python-app.yml/badge.svg)](https://github.com/jermwatt/quickbatch/actions/workflows/python-app.yml)

# quickbatch

quickbatch is an ultra-simple command-line tool for large batch processing and transformation. It allows you to scale any `processor` function that needs to be run over a large set of input data, enabling batch/parallel processing of the input with minimal setup and teardown.

- [Why use quickbatch](#why-use-quickbatch)
- [Installation](#installation) 
- [Usage](#usage)
- [Running quickbatch](#running-quickbatch)


## Why use quickbatch

quickbatch aims to be

- **dead simple to use:** versus standard cloud service batch transformation services that require significant configuration / service understanding

- **ultra fast setup:** versus setup of heavier orchestration tools like `airflow` or `mlflow`, which may be a hinderance due to time / familiarity / organisational constraints

- **100% portable:** - use quickbatch on any machine, anywhere

- **processor-invariant:** quickbatch works with arbitrary processes, not just machine learning or deep learning tasks.

- **transparent and open source:** quickbatch uses Docker under the hood and only abstracts away the not-so-fun stuff - including instantiation, scaling, and teardown.  you can still monitor your processing using familiar Docker command-line arguments (like `docker service ls`, `docker service logs`, etc.).


## Installation

To install quickbatch, simply use `pip`:

```bash
pip install quickbatch
```

## Usage

To use quickbatch, you need to define a `processor.py` file and a `config.yaml` file containing the necessary paths and parameters.

### `processor.py`

Create a `processor.py` file with the following pattern:

```python
import ...

def processor(todos):
    # Processor code
```

quickbatch will essentially point your `processor.py` at the `input_path` defined in your `config.yaml` and process this input in parallel at a scale given by your choice of `num_processors`.  Output will be written to the `output_path` specified in the configuration file.

### `config.yaml`

Create a `config.yaml` file with the following structure:

```yaml
data:
  input_path: /path/to/your/input/data
  output_path: /path/to/your/output/data
  log_path: /path/to/your/log/file

queue:
  feed_rate: <int - number of examples processed per processor instance>
  order_files: <boolean - whether or not to order input files by size>

processor:
  processor_path: /path/to/your/processor/processor.py
  num_processors: <int - instances of processor to run in parallel>
```

### Running quickbatch

To run quickbatch, execute the following command in your terminal:

```bash
quickbatch /path/to/your/config.yaml
```


 
 


