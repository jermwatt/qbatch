from pathlib import Path
import sys
import os
base_path = str(Path(__file__).parent.parent)
sys.path.append(str(base_path))


def test_quick_batch_test_1():
    config_path = f'{base_path}/tests/test_configs/test_1/quick_batch_github.yaml'

    if os.getenv('GITHUB_ACTIONS') == 'true':
        config_path = f'{base_path}/tests/test_configs/test_1/quick_batch_github.yaml'

    else:
        config_path = f'{base_path}/tests/test_configs/test_1/quick_batch_local.yaml'

    # delete contents of f'{base_path}/tests/test_data/output_data' but not folder
    for file_name in os.listdir(f'{base_path}/tests/test_data/output_data/test_1'):
        os.remove(f'{base_path}/tests/test_data/output_data/test_1/{file_name}')

    # rub quick_batch
    from quick_batch import main
    main.main(config=config_path)

    # load in output data file names from
    # f'{base_path}/tests/test_data/output_data'
    output_data = os.listdir(f'{base_path}/tests/test_data/output_data/test_1')

    # load in expected output data file names from
    # f'{base_path}/tests/test_data/expected_output_data'
    expected_output_data = os.listdir(f'{base_path}/tests/test_data/expected_output_data/test_1')

    # loop through each file name in output_data,
    # assert that it is in expected_output_data
    for file_name in output_data:
        assert file_name in expected_output_data

    # loop through each file in output_data, load in contents,
    # and assert is same as expected
    for file_name in output_data:
        with open(f'{base_path}/tests/test_data/output_data/test_1/{file_name}', 'r') as f:
            output_data_contents = f.read()
        with open(f'{base_path}/tests/test_data/expected_output_data/test_1/{file_name}', 'r') as f:
            expected_output_data_contents = f.read()
        assert output_data_contents == expected_output_data_contents



# def assert_length_similarity(text1, text2, threshold=90):
#     len1 = len(text1)
#     len2 = len(text2)

#     # Calculate the percentage difference between the lengths
#     percentage_diff = abs(len1 - len2) / max(len1, len2) * 100

#     # Compare against the threshold
#     if percentage_diff <= threshold:
#         return True
#     else:
#         return False

# def test_quick_batch_test_2():
#     config_path = f'{base_path}/tests/test_configs/test_2/quick_batch_github.yaml'

#     if os.getenv('GITHUB_ACTIONS') == 'true':
#         config_path = f'{base_path}/tests/test_configs/test_2/quick_batch_github.yaml'

#     else:
#         config_path = f'{base_path}/tests/test_configs/test_2/quick_batch_local.yaml'

#     # delete contents of f'{base_path}/tests/test_data/output_data' but not folder
#     for file_name in os.listdir(f'{base_path}/tests/test_data/output_data/test_2'):
#         os.remove(f'{base_path}/tests/test_data/output_data/test_2/{file_name}')

#     # rub quick_batch
#     from quick_batch import main
#     main.main(config=config_path)

#     # load in output data file names from
#     # f'{base_path}/tests/test_data/output_data'
#     output_data = os.listdir(f'{base_path}/tests/test_data/output_data/test_2')

#     # load in expected output data file names from
#     # f'{base_path}/tests/test_data/expected_output_data'
#     expected_output_data = os.listdir(f'{base_path}/tests/test_data/expected_output_data/test_2')

#     # loop through each file name in output_data,
#     # assert that it is in expected_output_data
#     for file_name in output_data:
#         assert file_name in expected_output_data

#     # loop through each file in output_data, load in contents,
#     # and assert is same as expected
#     for file_name in output_data:
#         with open(f'{base_path}/tests/test_data/output_data/test_2/{file_name}', 'r') as f:
#             output_data_contents = f.read()
#         with open(f'{base_path}/tests/test_data/expected_output_data/test_2/{file_name}', 'r') as f:
#             expected_output_data_contents = f.read()
            
#         # assert 
#         assert assert_length_similarity(output_data_contents, expected_output_data_contents)
