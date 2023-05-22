import sys
import os
import inspect
import yaml
import importlib.util
from .progress_logger import log_exceptions


@log_exceptions
def check_config_data_paths(config_path):
    # import config variables
    with open(config_path, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    # check that data paths in config file entries are valid
    input_path = config["data"]["input"]["machine_path"]
    output_path = config["data"]["output"]["machine_path"]

    # check that input path exists
    if not os.path.isdir(input_path):
        print("FAILURE: input path does not exist")
        sys.exit(1)
    else:
        print("SUCCESS: config input path exists")

    # check that output path exists
    if not os.path.isdir(output_path):
        print("FAILURE: output path does not exist")
        sys.exit(1)
    else:
        print("SUCCESS: config output path exists")

    # check that input path is not empty
    if not os.listdir(input_path):
        print("FAILURE: input path is empty")
        sys.exit(1)
    else:
        print("SUCCESS: config input path is not empty")
        # files = os.listdir(input_path)
        # print(f"SUCCESS: files in input path: {files}")

    return input_path, output_path


@log_exceptions
def check_files(config_path, processor_path):
    # check if file exists
    if not os.path.isfile(config_path):
        print("FAILURE: config_path file does not exist")
        sys.exit(1)
    else:
        print("SUCCESS: config_path file exists")

    # check if processor exists
    if not os.path.isfile(processor_path):
        print("FAILURE: processor_path file does not exist")
        sys.exit(1)
    else:
        print("SUCCESS: processor_path file exists")


# check to make sure processor.py is valid
# for now - that it contains a function named 'processor'
@log_exceptions
def check_processor(processor):
    # Module name to check for
    module_name = 'processor'

    # Load the module dynamically
    spec = importlib.util.spec_from_file_location(module_name, processor)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Check if the 'processor' function is defined in the module
    if 'processor' in dir(module):
        # Get the 'processor' function object
        processor_func = getattr(module, 'processor')

        # Check if it is a function
        if inspect.isfunction(processor_func):
            print(f"SUCCESS: The module '{module_name}' does contain a function named 'processor'.")
        else:
            print(f"FAILURE: The module '{module_name}' does NOT contain a function named 'processor'.")
            sys.exit(1)
    else:
        print(f"FAILURE: The module '{module_name}' does NOT contain a function named 'processor'.")
        sys.exit(1)
