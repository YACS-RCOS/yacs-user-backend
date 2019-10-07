import json
class MessageFactory(object):
    @staticmethod
    def successMsg(content:dict):
        result = {"success" : True, "errMsg" : None, "content" : content}
        return json.dumps(result)

    @staticmethod
    def errMsg(errMsg : str,content = None):
        result = {"success": False, "errMsg": errMsg, "content": content}
        return json.dumps(result)