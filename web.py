import os
from bottle import run, get, post, request


messages = []


@get('/')
def get_index():
    return 'welcome to echo'


@get('/messages')
def get_messages():
    return {'messages': messages}


@get('/clear')
def get_messages():
    global messages
    messages = [{'name': 'echo', 'message': 'make what you want of this'}]
    return {'messages': messages}


@post('/message')
def post_message():
    global messages
    message = None
    try:
        message = request.json
        if message is None:
            message = {'user': 'echo', 'message': 'Huh, say something?'}
    except Exception as e:
        message = {'user': 'echo', 'message': 'Huh, what?'}
    messages.append(message)
    messages = messages[-10:]
    return {'messages': messages}


@post('/echo')
def post_echo():
    message = None
    try:
        message = request.json
        if message is None:
            message = {'call': 'echo', 'message': 'Huh, say something?'}
    except Exception as e:
        message = {'call': 'echo', 'message': 'Huh, crap!'}
    return message


@get('/warranty')
def get_warranty():
    try:
        serial = request.query.Serial
        if serial is None:
            device = {'call': 'warranty', 'message': 'Huh, missing something?'}
        else:
            device = {
                "ProductId": serial,
                "BaseProductId": "Laptops-and-netbooks/ThinkPad-T-Series-laptops/ThinkPad-T430s",
                "MachineType": "2356",
                "Mode": "GUU",
                "ProductName": "T430s Laptop (ThinkPad)",
                "ProductImage": "//support.lenovo.com/~/media//Images/ProdImageLaptops/thinkpad_t430s",
                "Warranties": [
                    {
                        "Country": "US",
                        "Channel": "10",
                        "Code": "3EZ",
                        "Description": "This product has a three year limited warranty and is entitled to depot repair service. Customers may call their local service center for more information. Dealers may provide carry-in repair for this product. Batteries have a one year warranty.",
                        "Start": "2015-03-30T00:00:00",
                        "End": "2018-04-08T00:00:00"
                    },
                    {
                        "Country": "US",
                        "Channel": "10",
                        "Code": "1EZBAT",
                        "Description": "The battery included within this product is entitled to a 1 year CRU/Depot warranty.  Please note that this may differ from the warranty of the base product itself.",
                        "Start": "2015-03-30T00:00:00",
                        "End": "2016-04-08T00:00:00"
                    }
                ]
            }
    except Exception as e:
        device = {'call': 'warranty', 'message': 'Huh, crap!'}
    return device


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))