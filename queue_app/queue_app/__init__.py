from flask import Flask
import queues_init
import yaml


# instantiate app
app = Flask(__name__)


# import config variables
with open('/usr/src/configs/quick_batch.yaml', "r") as yaml_file:
    config = yaml.safe_load(yaml_file)


# extract required params
app.path_to_feed = config["queue_app"]["path_to_feed"]
app.file_type = config["queue_app"]["file_type"]
app.order_files = config["queue_app"]["order_files"]
app.feed_rate = config["queue_app"]["feed_rate"]
app.empty_trigger = 0


# instantiate queues
queues_init.create_queues(app)

# prevent circular imports for api connections
from . import app

# report startup success to terminal
print('queue_app node has started', flush=True)
