from flask import Flask

app = Flask(__name__)


@app.route("/task_01")
def task_01():
    return "<h1>Task_01 and Jenkins Success!!! hello world</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="10103")
