from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import til_generator
import webbrowser

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/til", methods=["POST"])
def get_TIL():
    sentences_receive = request.form["sentences_give"]
    if int(sentences_receive) > 10000:
        return jsonify({"TIL": "10,000문장 초과하시면 안됩니다!!!"})
    elif int(sentences_receive) < 1:
        return jsonify({"TIL": "1문장 미만은 안됩니다,,,"})
    result = til_generator.run(int(sentences_receive), True)
    return jsonify({"TIL" : result})

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run('0.0.0.0', port=5000, debug=True)