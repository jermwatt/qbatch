from flask import Flask
import subprocess
import yaml


def create_app():
    app = Flask(__name__)

    # attach container id
    container_id = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    container_id = eval(str(container_id)).decode('utf-8').strip('\n')
    app.container_id = container_id

    # # import config variables
    # with open('/usr/src/configs/quick_batch.yaml', "r") as yaml_file:
    #     config = yaml.safe_load(yaml_file)

    # # extract required params
    # app.path_to_feed = config["queue_app"]["path_to_feed"]
    # app.save_location = config["queue_app"]["save_location"

    # report startup success to terminal
    print(f'controller_app running on container {app.container_id} has started',
        flush=True)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=False, port=80, threaded=True)
