import fire
from utilities.manage_setup import setup_client
from utilities.manage_setup import reset_workspace
from utilities.manage_setup import setup_workspace
from utilities.manage_queue import monitor_queue


def main(config="",
         processor=""):
    # setup
    client, input_path, output_path = setup_client(config, processor)

    # reset workspace
    reset_workspace(client)

    # create workspace
    queue_service, processor_service = setup_workspace(client,
                                                       config,
                                                       processor,
                                                       input_path,
                                                       output_path)

    # scale up processor service
    processor_service.scale(2)

    # monitor queue
    monitor_queue(client)


if __name__ == '__main__':
    fire.Fire(main)
