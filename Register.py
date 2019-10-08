from MessageFactory import MessageFactory as msg
from database import DB


def register(form):
    db = DB()

    name = form['name']
    email = form['email']
    phone = form['phone']
    password = form['password']
    major = form['major']
    degree = form['degree']

    if len(db.getUser(email=email)) != 0:
        return msg.errMsg("User alreadt exists.")

    db.addUser(name, email, phone, password, major, degree)

    return msg.successMsg({"msg": "User added successfully."})
