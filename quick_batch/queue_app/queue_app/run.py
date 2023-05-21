# for local development
import sys
import os

# Get the parent directory of my_package
package_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(package_directory)

# Add the parent directory to sys.path
sys.path.append(parent_directory)

from queue_app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80, threaded=True)
