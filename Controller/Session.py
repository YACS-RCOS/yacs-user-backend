from common import *
from Model.Session import Session as SessionModel
from Model.User import User as UserModel
from datetime import datetime
import View.Message as msg

def deleteSession(form):
    if not checkKeys(form, ['sessionID']):
        return msg.errMsg("Please check your request body.")

    sessions = SessionModel()

    givenSessionID = form['sessionID']
    endTime = datetime.utcnow()
    sessions.endSession(givenSessionID,endTime)
    return msg.successMsg({"sessionID":givenSessionID,"endTime": endTime})


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
    startTime = datetime.utcnow()
    sessions.startSession(newSessionID, uid, startTime)
    return msg.successMsg({"sessionID" : newSessionID, "uid" : uid, "startTime": str(startTime)})

