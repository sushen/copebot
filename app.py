import sys
from flask import Flask, request
from pprint import pprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return '''
    <h2> I am focus</h2>
    <h1> I am determent to do business with this chatbot. </h1>
    
    ''', 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    return "ok", 200


def log(message):
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)