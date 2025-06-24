from flask import make_response, jsonify


def response_data(data, code, serialized=False):
    headers = {
        "Content-Type": "text/json",
    }
    if serialized == True:
        data = [item.serialize() for item in data]
        return make_response(jsonify(data), code, headers)
    return make_response(jsonify(data), code, headers)


def response_msg(text: str = None, code=500):
    headers = {
        "Content-Type": "text/json",
    }
    if text:
        msg = {"msg_": text}
    else:
        msg = {"msg_": "Internal Server Error"}

    return make_response(jsonify(msg), code, headers)
