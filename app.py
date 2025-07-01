from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_msg = data.get("message", "")
    bot_reply = bot.get_response(user_msg)

    return jsonify({"reply": bot_reply})

@app.route("/reload", methods=["POST"])
def reload_faq():
    bot.reload_faq()
    return jsonify({"status" : "SUCCESS!"})

if __name__ == "__main__":
    app.run(debug=True)