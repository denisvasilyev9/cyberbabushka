from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "привет": "Здорово, внучек!",
    "как дела": "Да вот, железяку новую починила!",
    "где купить хлеб": "Да в Яндекс Лавке закажи, чо бегать-то!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response")
def get_response():
    msg = request.args.get("msg", "").lower()
    response = responses.get(msg, "Чё ты там буровишь, внучек?")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
