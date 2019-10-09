#!/usr/bin/python3
from flask import Flask, request
from config import *
from Register import *
app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def registerRoute():
    return register(request.json)

if __name__ == '__main__':
    app.run(debug=APP_DEBUG_MODE,host=APP_HOST)