from utilities import base_directory, processor_path, controller_path, \
    queue_path
from .progress_logger import log_exceptions


# start queue_app docker container with interactive terminal
@log_exceptions
def startup_queue_app(client, config_path):
    queue_container = client.containers.run(
        'quick_batch_queue_app',
        detach=True,
        name='queue_app',
        tty=True,
        stdin_open=True,
        ports={'80/tcp': 80},
        volumes={
            queue_path:
            {'bind': '/my_app', 'mode': 'rw'},
            config_path:
            {'bind': '/my_app/config.yaml', 'mode': 'rw'},
        },
        command='python /my_app/run.py'
        )

    return queue_container
