import os

setts = []

controlVar = "Y"
defaultPart = ""
coloredPart = ""
outlinePart = ""
eventPart = ""
way = os.getcwd()

config = open(way + "/config.cfg")
configText = config.read()


def default(inputText):
    global defaultPart, configText

    defaultSample = configText[configText.find("|default|")+9:configText.find("/default|")]
    defaultSample = defaultSample.replace("variable", inputText)
    defaultPart = defaultSample    


def textColor(color):
    global coloredPart, configText

    if color != 'nothing':
        defaultSample = configText[configText.find("|color|")+7:configText.find("/color|")]
        defaultSample = defaultSample.replace("colorvar", color)
        coloredPart = defaultSample
    else:
        pass

def textOutline(outline):
    global outlinePart, configText

    if outline != 'nothing':
        defaultSample = configText[configText.find("|outline|")+9:configText.find("/outline|")-1]
        defaultSample = defaultSample.replace("value", outline)
        outlinePart = defaultSample
    else:
        pass

def clickEvent(event):
    global eventPart, configText
    if event != '':
       defaultSample = configText[configText.find("|event|")+7:configText.find("/event|")-1]
       defaultSample = defaultSample.replace("yourcommand", event)
       eventPart = defaultSample
    else:
        pass


def textmaker(inputText, color, outline, event):
    default(inputText)
    textColor(color)
    textOutline(outline)
    clickEvent(event)
    return defaultPart + coloredPart + outlinePart + eventPart + '}"'




