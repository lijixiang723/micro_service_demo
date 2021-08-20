from flask import Flask

app = Flask(__name__)


@app.route("/demo_01")
def task_01():
    return "<h1>CI/CD Demo</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="10104")
