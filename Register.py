from MessageFactory import MessageFactory as msg
from database import DB


def register(form):
    db = DB()

    try:
        name = form['name']
        email = form['email']
        phone = form['phone']
        password = form['password']
        major = form['major']
        degree = form['degree']
    except KeyError:
        return msg.errMsg("Please check your request keys.")

    if password.split() == "":
        return msg.errMsg("Password cannot be empty.")

    if len(db.getUser(email=email)) != 0:
        return msg.errMsg("User alreadt exists.")

    db.addUser(name, email, phone, password, major, degree)

    return msg.successMsg({"msg": "User added successfully."})
