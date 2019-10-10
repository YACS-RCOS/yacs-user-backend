#!/usr/bin/python3
from flask import Flask, request
from config import *
import Controller.User as userController
import Controller.Session as sessionController

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def addUser():
    return userController.addUser(request.json)

@app.route('/users', methods=['GET'])
def getUser():
    return userController.getUser(request.json)

@app.route('/sessions', methods=['POST'])
def login():
    return sessionController.addSession(request.json)


if __name__ == '__main__':
    app.run(debug=APP_DEBUG_MODE,host=APP_HOST)