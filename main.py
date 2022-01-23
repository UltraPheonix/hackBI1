from firebase import firebase


firebase = firebase.FirebaseApplication("https://hackim-42ce9-default-rtdb.firebaseio.com/", None)
class instantMessage:
    x = "x"
    Channel = 'name'
    logs = {}
    name = ''
    finalMessage = []
    def sendMessage(Message, Channel1):
        if Channel1 in instantMessage.channelArray():
            instantMessage.finalMessage = [instantMessage.name, Message]
            instantMessage.Channel = Channel1
            instantMessage.logs[Channel1].append(instantMessage.finalMessage)
            firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, instantMessage.finalMessage)
        else:
            instantMessage.createChannel(Channel1)
            instantMessage.finalMessage = [instantMessage.name, Message]
            instantMessage.Channel = Channel1
            instantMessage.logs[Channel1].append(instantMessage.finalMessage)
            firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, instantMessage.finalMessage)
    def createChannel(Channel1):
        firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, "" )
        instantMessage.channelArray()
        instantMessage.logs[Channel1] = []
    def getCurrentMessage():
        y = ''
        instantMessage.x = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/'+ instantMessage.Channel, None))
        instantMessage.logs[instantMessage.Channel].append(str(instantMessage.x[0] +' '+ instantMessage.x[1]))
        return str(firebase.get('/hackim-42ce9-default-rtdb/Messages/'+ instantMessage.Channel, None))
    def messageLogs():
        logs1 = {}
        channels = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', None))
        for channel in channels:
            messages = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', channel))
            logs1[channel] = instantMessage.finalMessage

        instantMessage.logs = logs1
    def channelArray():
        x = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', None))
        return x
    def getMessages():
        instantMessage.messageLogs()
        return instantMessage.logs[instantMessage.Channel]