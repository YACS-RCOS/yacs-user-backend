from Model.UserEvent import UserEvent as UserEvents
import View.Message as msg
from common import *

def addEvent(form):
    userEvents = UserEvents()

    if not checkKeys(form, ['uid','eventID','data','createdAt']):
        return msg.errMsg("Invalid request body.")


    uid = form['uid']
    eventID = form['eventID']
    data = form['data']
    timestamp = form['createdAt']
    addEventResult = userEvents.addEvent(uid=uid,eventID=eventID,data=data,timestamp=timestamp)

    if addEventResult == None:
        return msg.errMsg("Failed to add event.")

    return msg.successMsg({"msg": "Event added successfully."})
