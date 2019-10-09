from Model.User import User as UserModel
import View.Message as msg
from common import *
def getUser(form):
    userModel = UserModel()

    if not (checkKeys(form, ['uid']) or checkKeys(form, ['email'])):
        return msg.errMsg("Please specify uid or email.")

    if 'uid' in form.keys():
        result = userModel.getUser(uid=form['uid'])
    else:
        result = userModel.getUser(email=form['email'])

    if result == None:
        return msg.errMsg("Failed to find user.")

    if len(result) == 0:
        return msg.errMsg("This user doesn't exists.")

    user = result[0]
    return msg.successMsg({'uid':user[0],'name':user[1],'email': user[2], 'phone' : user[3], 'major': user[4], 'degree': user[5]})



def addUser(form):
    userModel = UserModel()

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

    findUser = userModel.getUser(email=email)
    if findUser == None:
        return msg.errMsg("Failed to find user.")

    if len(findUser) != 0:
        return msg.errMsg("User alreadt exists.")

    ret = userModel.addUser(name, email, phone, password, major, degree)
    if ret != None:
        return msg.successMsg({"msg": "User added successfully."})
    else:
        return msg.errMsg("Failed to add user.")