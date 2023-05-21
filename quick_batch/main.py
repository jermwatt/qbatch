import fire
from utilities import param_checks
from utilities import docker_setup


def main(config="",
         processor=""):

    # check that input files exist
    param_checks.check_files(config, processor)

    # create docker client
    client = docker_setup.create_client()

    # build images
    docker_setup.build_processor_image(client)
    docker_setup.build_queue_image(client)
    docker_setup.build_controller_image(client)
    
    # startup containers
    
    
    

if __name__ == '__main__':
    fire.Fire(main)
