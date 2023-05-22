import json
import time
from .progress_logger import log_exceptions
from .manage_containers import remove_all_containers
from .manage_networks import remove_network
from .manage_services import remove_all_services


@log_exceptions
def get_current_queue_lengths(client):
    # Get the list of running containers for the service
    queue_app_container = client.containers.list(filters={'label': 'com.docker.swarm.service.name=queue_app'})

    # Assuming there is only one container for the service
    if queue_app_container:
        queue_app_container = queue_app_container[0]
        command = 'curl -s localhost:80'
        response = queue_app_container.exec_run(command)
        response = json.loads(response.output.decode('utf-8'))
        return response
    else:
        print("No running containers found for the service.")
        return None


# watch feed_queue_length, when it reaches 0, stop the processor service
def monitor_queue(client):
    time.sleep(5)
    while True:
        response = get_current_queue_lengths(client)
        feed_queue_length = response['feed_queue_length']
        print(feed_queue_length, flush=True)
        if feed_queue_length == 0:

            remove_all_services(client)
            remove_all_containers(client)
            remove_network(client)

            break
        time.sleep(5)
