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
    defaultSample = defaultSample.replace("variable", inputText.get())
    defaultPart = defaultSample    


def textColor(color):
    global coloredPart, configText

    if color != 'N':
        defaultSample = configText[configText.find("|color|")+7:configText.find("/color|")-1]
        defaultSample = defaultSample.replace("colorvar", color.get())
        coloredPart = defaultSample
    

def textOutline(outline):
    global outlinePart, configText

    Outline = outline.get()

    if Outline != 'N':
        if Outline.find(',') != 1:
            count = Outline.count(',') + 1
            setts = Outline.split(',')
            for i in range(count):
                defaultSample = configText[configText.find("|outline|") + 9:configText.find("/outline|") - 1]
                defaultSample = defaultSample.replace("value", setts[i])
                outlinePart += defaultSample
        else:
            defaultSample = configText[configText.find("|outline|")+5:configText.find("/outline|")-1]
            defaultSample = defaultSample.replace("value", Outline)
            outlinePart = defaultSample


def clickEvent(event):
    global eventPart, configText
    
    if event != 'N':
       defaultSample = configText[configText.find("|event|")+6:configText.find("/event|")-1]
       defaultSample = defaultSample.replace("yourcommand", event.get())
       eventPart = defaultSample


def textmaker(inputText, color, outline, event):
    default(inputText)
    textColor(color)
    textOutline(outline)
    clickEvent(event)
    return "There you go: " + defaultPart + coloredPart + outlinePart + eventPart + '}"'




