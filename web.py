from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import til_generator

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/til", methods=["POST"])
def get_TIL():
    sentences_receive = request.form["sentences_give"]
    result = til_generator.run(int(sentences_receive))
    return jsonify({"TIL" : result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)