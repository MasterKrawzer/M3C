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
    
    defaultSample = configText[configText.find("|default|")+9:configText.find("/default|")-1]
    defaultSample = defaultSample.replace("variable", inputText)
    defaultPart = defaultSample    


def textColor(color):
    global coloredPart, configText

    if color != 'N':
        defaultSample = configText[configText.find("|color|")+7:configText.find("/color|")-1]
        defaultSample = defaultSample.replace("colorvar", color)
        coloredPart = defaultSample
    

def textOutline(outline):
    global outlinePart, configText
    
    if outline != 'N':
        if outline.find(',') != 1:
            count = outline.count(',') + 1
            setts = outline.split(',')
            for i in range(count):
                defaultSample = configText[configText.find("|outline|") + 9:configText.find("/outline|") - 1]
                defaultSample = defaultSample.replace("value", setts[i])
                outlinePart += defaultSample
        else:
            defaultSample = configText[configText.find("|outline|")+5:configText.find("/outline|")-1]
            defaultSample = defaultSample.replace("value", outline)
            outlinePart = defaultSample


def clickEvent(event):
    global eventPart, configText
    
    if event != 'N':
       defaultSample = configText[configText.find("|event|")+6:configText.find("/event|")-1]
       defaultSample = defaultSample.replace("yourcommand", event)
       eventPart = defaultSample


def textmaker(inputText, color, outline, event):
    default(inputText)
    textColor(color)
    textOutline(outline)
    clickEvent(event)
    return "There you go: " + defaultPart + coloredPart + outlinePart + eventPart + '}"'




