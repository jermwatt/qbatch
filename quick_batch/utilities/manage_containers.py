from utilities import base_directory, processor_path, controller_path, \
    queue_path


def startup_queue_app(client):
    # start queue_app docker container with interactive terminal
    queue_container = client.containers.run(
        'quick_batch_queue_app',
        detach=True,
        name='queue_app',
        tty=True,
        stdin_open=True,
        ports={'80/tcp': 80},
        volumes={
            queue + '/processor_app': 
            {'bind': '/my_app', 'mode': 'rw'},
            base_directory + '/processor.py':
            {'bind': '/my_app/processor.py', 'mode': 'rw'},
        },
        command='python /my_app/run.py'
        )
    
    return queue_container