from utilities import base_directory, processor_path, controller_path, \
    queue_path
from .progress_logger import log_exceptions
import os 


# remove all docker containers
@log_exceptions
def remove_all_containers(client):
    for container in client.containers.list(all=True):
        container.remove(force=True)


# start queue_app docker container with interactive terminal
@log_exceptions
def startup_queue_app(client, config_path, input_path):
    queue_container = client.containers.run(
        'quick_batch_queue_app',
        detach=True,
        name='queue_app',
        tty=True,
        stdin_open=True,
        ports={'80/tcp': 80},
        volumes={
            queue_path + '/queue_app':
            {'bind': '/my_app', 'mode': 'ro'},
            config_path:
            {'bind': '/my_configs/config.yaml', 'mode': 'ro'},
            input_path:
            {'bind': '/my_data/input', 'mode': 'ro'}
        },
        command='python /my_app/run.py'
        )

    return queue_container


# start queue_app docker container with interactive terminal
@log_exceptions
def startup_processor_app(client, config_path, input_path, output_path):
    # start processor_app docker container with interactive terminal
    processor_container = client.containers.run(
        'quick_batch_processor_app',
        detach=True,
        name='processor_app',
        tty=True,
        stdin_open=True,
        ports={'81/tcp': 81},
        volumes={
            processor_path + '/processor_app':
            {'bind': '/my_app', 'mode': 'ro'},
            config_path:
            {'bind': '/my_configs/config.yaml', 'mode': 'ro'},
            input_path:
            {'bind': '/my_data/input', 'mode': 'ro'},
            output_path:
            {'bind': '/my_data/output', 'mode': 'rw'},
            base_directory + '/processor.py':
            {'bind': '/my_app/processor.py', 'mode': 'ro'},
        },
        command='python /my_app/run.py'
        )

    return processor_container
