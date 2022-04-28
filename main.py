# -*- coding: utf-8 -*-

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_docker():
    # return "Hello,Docker!"
    return render_template('hello.html',name='Docker')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
