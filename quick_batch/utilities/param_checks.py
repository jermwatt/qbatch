import sys
import os
import yaml


def check_config_data_paths(config_path):
    # import config variables
    with open(config_path, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    # check that data paths in config file entries are valid
    input_path = config["data"]["input"]["path_to_input"]
    output_path = config["data"]["output"]["path_to_output"]

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
        files = os.listdir(input_path)
        print(f"SUCCESS: files in input path: {files}")


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
        
    # check config data paths
    check_config_data_paths(config_path)
