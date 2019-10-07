from flask import Flask
from Register import *
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    return

if __name__ == '__main__':
    app.run()