# from processor_app import app
from activate_process import activate
from flask import Flask
import yaml
import subprocess

def create_app():
    app = Flask(__name__)

    # attach container id
    container_id = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    container_id = eval(str(container_id)).decode('utf-8').strip('\n')
    app.container_id = container_id

    # # import config variables
    # with open('/usr/src/configs/quick_batch.yaml', "r") as yaml_file:
    #     config = yaml.safe_load(yaml_file)

    # app.path_to_feed = config["data"]["input"]["path_to_input"]
    # app.feed_rate = config["data"]["input"]["feed_rate"]
    # app.save_location = config["data"]["output"]["path_to_output"]

    # report startup success to terminal
    print('processor_app running on container {app.container_id} has started',
        flush=True)
    
    return app


if __name__ == '__main__':
    app = create_app()
    # activate(app)
    app.run(host='0.0.0.0', debug=False, port=80, threaded=True)
