import sys
from flask import Flask, request
from pprint import pprint
from pymessenger import Bot


Facebook_Access_Token = 'EAACvvGBVPhEBAIpqcxK5NkKZCa2Bmwlrblp01Tora2BFvLqCNhxmYoxoeVYvyiaxIfW05TL4BCPMlxT4QjzDsaUumtHZCcnhvExSoa6y5I6ATmHJJaDPj4b7rZAtPZAbftEA5vgcCKuYj9xzn0twsQUEZBrMybJZCIPFQCdvx60QZDZD'
bot = Bot(Facebook_Access_Token)

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

    if data['object'] == ['page']:
        for entry in data['entry']:
            for messaging_event in data ['messaging']:

                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'No text'

                response = messaging_text
                bot.send_text_message(recipient_id, response)



    return "ok", 200


def log(message):
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)