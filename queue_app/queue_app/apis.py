import app
from flask import jsonify, request
import queue


@app.route('/send_object_paths', methods=['GET'])
def send_object_paths():
    # feeder queue
    if not app.feeder_queue.empty():
        # get next object data paths
        object_paths = []
        for i in range(app.feed_rate):
            # collect next path
            next_path = app.feeder_queue.get()
            object_paths.append(next_path)

            # update wip queue
            app.wip_queue.put(next_path)

            # update counters
            app.wip_queue_length += 1
            app.feed_queue_length -= 1

        return jsonify({'object_paths': object_paths})
    else:
        if app.empty_trigger == 0: 
            app.empty_trigger += 1

            # send empty queue message to container log
            print('feeder queue is empty', flush=True)

        # return news to requester
        return 'feeder queue is empty'


# receive message from processor of completion
@app.route('/done_from_processor', methods=['POST'])
def done_from_processor():
    # grab new datapoint from post
    try:
        # get datapoint from request
        data = request.json['data']

        # update done queue
        app.done_queue.put("'" + data + "'")

        # update wip queue
        updated_queue = queue.Queue()
        while not app.wip_queue.empty():
            item = app.wip_queue.get()
            if item not in data:
                updated_queue.put(item)

        # replace existing wip qeue
        app.wip_queue = updated_queue

        # update counters
        for d in data:
            app.feed_queue_length -= 1
            app.done_queue_length += 1
            app.wip_queue_length -= 1

        return jsonify("200")
    except Exception as e:
        print(e, flush=True)
        return jsonify("400")


@app.route('/current_queue_lengths', methods=['GET'])
def current_queue_lengths():
    return jsonify({'feed_queue_length': app.feed_queue_length,
                    'wip_queue_length': app.wip_queue_length,
                    'done_queue_length': app.done_queue_length})
