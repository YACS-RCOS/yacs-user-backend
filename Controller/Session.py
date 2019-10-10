from common import *
from Model.Session import Session as SessionModel
from Model.User import User as UserModel

import View.Message as msg


def addSession(form):
    if not checkKeys(form,['email','password']):
        return msg.errMsg("Please check the inputs.")

    sessions = SessionModel()
    users = UserModel()

    (email,password)=(form['email'],form['password'])

    usersFounded = users.getUser(email=email,password=password)
    if usersFounded == None:
        return msg.errMsg("Failed to validate user information.")

    if len(usersFounded) == 0:
        return  msg.errMsg("Invalid email address or password.")

    uid = usersFounded[0][0]
    newSessionID = sessions.createSessionID()

    sessions.saveSession(newSessionID,uid)

