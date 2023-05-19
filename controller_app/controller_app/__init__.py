from flask import Flask
import queues_init
import yaml
import subprocess


# instantiate app
app = Flask(__name__)

# attach container id
container_id = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
container_id = eval(str(container_id)).decode('utf-8').strip('\n')
app.container_id = container_id


# import config variables
with open('/usr/src/configs/quick_batch.yaml', "r") as yaml_file:
    config = yaml.safe_load(yaml_file)

app.path_to_feed = config["queue_app"]["path_to_feed"]
app.save_location = config["queue_app"]["save_location"]

# report startup success to terminal
print('processor_app running on container {app.container_id} has started', 
      flush=True)

# prevent circular imports for api connections
from activate_process import activate
activate(app)
