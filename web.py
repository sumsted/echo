import os
from bottle import run, template, get, post, request


messages = []


@get('/')
def get_index():
    return 'hi'


@get('/messages')
def get_messages():
    return {'messages': messages}


@post('/message')
def post_message():
    global messages
    message = None
    try:
        message = request.json
        if message is None:
            message = {'message': 'Huh, say something?'}
    except Exception as e:
        message = {'message': 'Huh, what?'}
    messages.append(message)
    messages = messages[-10:]
    return {'messages': messages}


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
