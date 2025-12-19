from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") # hello лишнее, иначе не будет открываться localhost/
def hello_world():
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080) # был невалидный порт
