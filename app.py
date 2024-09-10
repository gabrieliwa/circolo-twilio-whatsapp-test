from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body("Hi there! How can I assist you?")
    else:
        msg.body("I'm not sure how to respond. Try saying 'hello'.")

    return str(resp)

if __name__ == "__main__":
    app.run()