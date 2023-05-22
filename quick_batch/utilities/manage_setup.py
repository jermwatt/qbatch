import time
from utilities.param_checks import check_files
from utilities.param_checks import check_config_data_paths
from utilities.param_checks import check_processor
from utilities import manage_images
from utilities.manage_containers import remove_all_containers
from utilities.manage_networks import remove_network
from utilities.manage_services import remove_all_services
from utilities.manage_swarm import leave_swarm
from utilities.manage_swarm import create_swarm
from utilities.manage_networks import create_network
from utilities.manage_services import create_queue_service
from utilities.manage_services import create_processor_service
from .progress_logger import log_exceptions


@log_exceptions
def setup_client(config, processor):
    # check that input files exist
    check_files(config, processor)

    # check config data paths
    input_path, output_path = check_config_data_paths(config)

    # check processor
    check_processor(processor)

    # create docker client
    client = manage_images.create_client()

    # build images
    manage_images.build_processor_image(client)
    manage_images.build_queue_image(client)

    return client, input_path, output_path


@log_exceptions
def reset_workspace(client):
    # remove all services
    remove_all_services(client)
    time.sleep(5)

    # remove all containers
    remove_all_containers(client)

    # remove network
    remove_network(client)

    # remove swarms
    leave_swarm(client)


@log_exceptions
def setup_workspace(client,
                    config,
                    processor,
                    input_path,
                    output_path):
    # create new swarm
    create_swarm(client)

    # create network
    create_network(client)
    time.sleep(5)

    # create queue service
    queue_service = create_queue_service(client,
                                         config,
                                         input_path)
    time.sleep(10)

    # create processor service
    processor_service = create_processor_service(client,
                                                 config,
                                                 input_path,
                                                 output_path,
                                                 processor)

    return queue_service, processor_service
