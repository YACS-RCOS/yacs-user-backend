from flask import Flask, request
from Register import *
app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def registerRoute():
    return register(request.json)

if __name__ == '__main__':
    app.run()