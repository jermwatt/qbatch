from pathlib import Path
import sys
import os

base_path = str(Path(__file__).parent.parent)
sys.path.append(str(base_path))


config_path = f'{base_path}/tests/test_configs/test_quick_batch_github.yaml'

if os.getenv('GITHUB_ACTIONS') == 'true':
    print("Running on GitHub Actions")
    config_path = f'{base_path}/tests/test_configs/test_quick_batch_github.yaml'

else:
    print("Running locally")
    config_path = f'{base_path}/tests/test_configs/test_quick_batch_local.yaml'

# delete contents of f'{base_path}/tests/test_data/output_data' but not folder
for file_name in os.listdir(f'{base_path}/tests/test_data/output_data'):
    os.remove(f'{base_path}/tests/test_data/output_data/{file_name}')


def test_quick_batch():
    # rub quickbatch
    from quick_batch import main
    main.main(config=config_path)

    # load in output data file names from
    # f'{base_path}/tests/test_data/output_data'
    output_data = os.listdir(f'{base_path}/tests/test_data/output_data')

    # load in expected output data file names from
    # f'{base_path}/tests/test_data/expected_output_data'
    expected_output_data = os.listdir(f'{base_path}/tests/test_data/expected_output_data')

    # loop through each file name in output_data,
    # assert that it is in expected_output_data
    for file_name in output_data:
        assert file_name in expected_output_data

    # loop through each file in output_data, load in contents,
    # and assert is same as expected
    for file_name in output_data:
        with open(f'{base_path}/tests/test_data/output_data/{file_name}', 'r') as f:
            output_data_contents = f.read()
        with open(f'{base_path}/tests/test_data/expected_output_data/{file_name}', 'r') as f:
            expected_output_data_contents = f.read()
        assert output_data_contents == expected_output_data_contents
