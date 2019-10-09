#!/usr/bin/python3
from flask import Flask, request
from config import *
import Controller.User as userController

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def addUser():
    return userController.addUser(request.json)

@app.route('/user', methods=['GET'])
def getUser():
    return userController.getUser(request.json)

if __name__ == '__main__':
    app.run(debug=APP_DEBUG_MODE,host=APP_HOST)