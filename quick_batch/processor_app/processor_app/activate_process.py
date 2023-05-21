import sys
import api_connects
import os
import processor


def activate(app):
    # report startup success to terminal
    print('node has started', flush=True)

    # set lifetime - number of objects this container 
    # can process before restart
    lifetime = 1000
    while lifetime > 0:
        # get next batch of file paths
        api_connects.request_object_paths(app)
        print('RETRIEVED: with', str(app.input_data), flush=True)
        print('RETRIEVED: with', str(app.file_paths_to_process), flush=True)

        # process each file path
        processor.processor(app)

        # update lifetime
        lifetime -= 1

        # print progress
        print('FINISHED: with', str(app.input_data), flush=True)

    # if reaching the lifetime end signal to orchestator
    # that a new container be built
    sys.exit(1)
