from Model.User import User as UserModel
import View.Message as msg
from common import *
def getUser(form):
    users = UserModel()
    pass



def addUser(form):
    users = UserModel()

    if not checkKeys(form, ['name', 'email', 'phone', 'password', 'major', 'degree']):
        return msg.errMsg("Please check your requests.")

    name = form['name']
    email = form['email']
    phone = form['phone']
    password = form['password']
    major = form['major']
    degree = form['degree']

    if password.strip() == "":
        return msg.errMsg("Password cannot be empty.")

    findUser = users.getUser(email=email)
    if findUser == None:
        return msg.errMsg("Failed to find user.")

    if len(findUser) != 0:
        return msg.errMsg("User already exists.")

    ret = users.addUser(name, email, phone, password, major, degree)
    if ret != None:
        return msg.successMsg({"msg": "User added successfully."})
    else:
        return msg.errMsg("Failed to add user.")