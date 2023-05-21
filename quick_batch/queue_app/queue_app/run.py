from flask import Flask
import queues_init
import subprocess
import yaml
import logging
import sys



def create_app():
    app = Flask(__name__)

    # Configure logging
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    # attach container id
    container_id = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    container_id = eval(str(container_id)).decode('utf-8').strip('\n')
    app.container_id = container_id

    # import config variables
    with open('/my_configs/queue_config.yaml', "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    # extract required params
    app.path_to_feed = '/my_data/input'
    app.file_type = config["data"]["input"]["file_type"]
    app.feed_rate = config["apps"]["feed_rate"]
    app.order_files = config["apps"]["queue"]["order_files"]
    app.empty_trigger = 0

    # instantiate queues
    queues_init.create_queues(app)

    # print out organized_datapaths for debugging
    print(f'organized_datapaths: {app.organized_datapaths}', flush=True)

    # report startup success to terminal
    print(f'queue_app running on container {app.container_id} has started',
          flush=True)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=False, port=80, threaded=True)
