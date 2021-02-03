from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route ("/sms", methods=['POST'])
def sms_reply():
    #fetch message
    msg = request.form.get('Body')

    #reply
    resp=MessagingResponse()
    resp.message("You said that:{}".format(msg))

    return str(resp)

if __name__=="__main__":
    app.run(debug=True)
    