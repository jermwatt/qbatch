import shutil
import os
import docker
from .progress_logger import log_exceptions
from utilities import base_directory, processor_path, \
    queue_path


# create client for docker
@log_exceptions
def create_client():
    return docker.from_env()


# build processor_app docker image
@log_exceptions
def build_processor_image(client):
    # copy processor requirements.txt to processor_app directory to roll into
    # dockerfile
    shutil.copyfile(os.path.join(base_directory, 'processor_requirements.txt'),
                    os.path.join(processor_path, 'processor_requirements.txt'))

    # create docker image for processor app - including user defined
    # requirements
    client.images.build(path=processor_path, tag='quick_batch_processor_app',
                        quiet=False)

    # remove processor_requirements.txt from the processor_path directory
    os.remove(os.path.join(processor_path, 'processor_requirements.txt'))


@log_exceptions
def build_queue_image(client):
    # create docker image for queue app - including user defined requirements
    client.images.build(path=queue_path, tag='quick_batch_queue_app',
                        quiet=False)
