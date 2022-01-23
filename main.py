from firebase import firebase

##Setting up overall firebase link
firebase = firebase.FirebaseApplication("https://hackim-42ce9-default-rtdb.firebaseio.com/", None)
class instantMessage:
    ## Making my vars
    x = "x"
    Channel = 'name'
    logs = {}
    name = ''
    finalMessage = []

    ##Send Message class
    def sendMessage(Message, Channel1):
        ##Sending to a existing channel
        if Channel1 in instantMessage.channelArray():
            instantMessage.finalMessage = [instantMessage.name, Message]
            instantMessage.Channel = Channel1
            instantMessage.logs[Channel1].append(instantMessage.finalMessage)
            firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, instantMessage.finalMessage)
        ## Sending to a non existing channel
        else:
            instantMessage.createChannel(Channel1)
            instantMessage.finalMessage = [instantMessage.name, Message]
            instantMessage.Channel = Channel1
            instantMessage.logs[Channel1].append(instantMessage.finalMessage)
            firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, instantMessage.finalMessage)

    ##creating a new channel
    def createChannel(Channel1):
        firebase.put('/hackim-42ce9-default-rtdb/Messages/', Channel1, "" )
        instantMessage.channelArray()
        instantMessage.logs[Channel1] = []

    ##Getting the current message 
    def getCurrentMessage():
        y = ''
        instantMessage.x = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/'+ instantMessage.Channel, None))
        instantMessage.logs[instantMessage.Channel].append(str(instantMessage.x[0] +' '+ instantMessage.x[1]))
        return str(firebase.get('/hackim-42ce9-default-rtdb/Messages/'+ instantMessage.Channel, None))

    ##Finding the history of the channel 
    def messageLogs():
        logs1 = {}
        channels = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', None))
        for channel in channels:
            messages = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', channel))
            logs1[channel] = instantMessage.finalMessage
        instantMessage.logs = logs1

    ##Making the channel array to turn into a dict
    def channelArray():
        x = list(firebase.get('/hackim-42ce9-default-rtdb/Messages/', None))
        return x

    ##Getting the messages 
    def getMessages():
        instantMessage.messageLogs()
        return instantMessage.logs[instantMessage.Channel]