from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say("Hi, welcome to Smile Dental! How can I help you today?")
    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)