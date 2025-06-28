from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "license" in user_input:
        reply = "To get a driver's license, you need a student permit, medical certificate, and pass the exam."
    elif "speeding" in user_input or "violation" in user_input:
        reply = "Speeding usually results in fines and possibly suspension depending on severity."
    elif "age" in user_input or "driving age" in user_input:
        reply = "You must be at least 17 years old to apply for a driver’s license in the Philippines."
    elif "drunk" in user_input or "alcohol" in user_input:
        reply = "Driving under the influence can lead to license revocation and criminal charges."
    else:
        reply = "I'm a class Bot. I can help with traffic rules, violations, and license requirements."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)