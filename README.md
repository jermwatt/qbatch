# quickbatch

quickbatch is an ultra-simple command-line tool for docker-scaling batch processing of large-scale data transformations. It allows you to scale any `processor` function that needs to be run over a large set of input data, enabling batch/parallel processing of the input.

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

quickbatch will essentially point your `processor.py` at the `input_path` in your `config.yaml` and process this input in parallel at a scale given by your choice of `num_processors`.  Output will be written to the `output_path` specified in the configuration file.

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

quickbatch uses Docker in the background, abstracting away the need to instantiate, scale up, and manage containers running your `processor` function. You can quickly start up your Dockerized parallel processing via Python, yet still monitor using familiar Docker command-line arguments (like `docker service ls`, `docker service logs`, etc.).

To run qbatch, execute the following command in your terminal:

```bash
quickbatch /path/to/your/config.yaml
```

## Common Use Cases

quickbatch is particularly useful for:

- Data transformation tasks (e.g., deep learning inference) that need to be performed on a large set of distinct examples.
- Deep learning inference on large datasets.
- Batch processing large backlogs of data.
- Processes that can be encapsulated in a single `processor.py` file, making orchestration tools like `airflow` overly complex.
- Scaling arbitrary processes, not limited to machine learning or deep learning tasks.
