from multiprocessing.dummy import Process
from main import instantMessage as im
import PySimpleGUI as sg
import threading
import time
x = ""
Channel_list_column = [
    [
        sg.Text("Channel Name"),
        sg.In(size=(25, 1), enable_events=True, key="Channels"),
        sg.Button("Create")
    ],
    [
        sg.Text("Name"),
        sg.In(size=(25, 1), enable_events=True, key="Name"),
        sg.Button("Set Name")
    ],
    [
        sg.Listbox(
            values=im.channelArray(), enable_events=True, size=(40, 20), key="ChannelList"
        )
    ],
]
Message_list_column = [
    [
        sg.Text("Message"),
        sg.In(size=(25, 1), enable_events=True, key="Message"),
        sg.Button("Send"),
        sg.Button("Refresh")
    ],
    {
        sg.Listbox(
            values=im.getMessages(), enable_events=True, size=(40, 20), key="MessageList"
        )
    },
]
layout = [
    [
        sg.Column(Channel_list_column),
        sg.VSeparator(),
        sg.Column(Message_list_column),
    ]
]

imwindow = sg.Window("Instant Messager", layout)
ChannelSelect = ""
def loop1():
    while True:
        event, values = imwindow.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Create":
            im.createChannel(values["Channels"])
            im.messageLogs()
            im.channelArray()
            imwindow['ChannelList'].update(im.channelArray())
        if event == "ChannelList":
            x = values['ChannelList'][0]
            im.Channel = x
            im.messageLogs()
            imwindow['MessageList'].update(im.getMessages())
        if event == "Send":
            im.sendMessage(values["Message"], im.Channel)
            imwindow['MessageList'].update(im.logs[im.Channel])
        if event == 'Set Name':
            im.name = (values['Name']) + ':'
            imwindow['MessageList'].update(im.logs[im.Channel])
        if event == 'Refresh':
            imwindow['MessageList'].update(im.logs[im.Channel])
            imwindow['MessageList'].update(im.getMessages())
            im.getCurrentMessage()
def loop2():
    while True:
        time
        im.getCurrentMessage()
        imwindow['MessageList'].update(im.logs[im.Channel])
        imwindow['MessageList'].update(im.getMessages())
Process(target=loop1()).start()
Process(target=loop2()).start()




