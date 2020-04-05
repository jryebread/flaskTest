from flask import Flask, render_template
from flask import request
import sys
from sys import stderr

def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

app = Flask(__name__)


@app.route("/")
def home():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print('USER IP IS: ', ip, file=sys.stderr)
    print_err("IP IS RECORDED AS: ", ip)
    return render_template("template.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":

    app.run(debug=True)
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR'])  # if behind a proxy