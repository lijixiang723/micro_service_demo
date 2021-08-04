from flask import Flask

app = Flask(__name__)


@app.route("/task_02")
def task_01():
    return "<h1>Task_02</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="10104")
