import sys
import api_connects


def activate(app):
    # report startup success to terminal
    print('node has started', flush=True)

    # set lifetime - number of objects this container 
    # can process before restart
    lifetime = 1000
    while lifetime > 0:
        api_connects.request_object_paths(app)
        lifetime -= 1
        print('FINISHED: with', str(app.input_data), flush=True)

    # if reaching the lifetime end signal to orchestator
    # that a new container be built
    sys.exit(1)
