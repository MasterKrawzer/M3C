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


def default(input_text):
    global defaultPart, configText

    default_sample = configText[configText.find("|default|")+9:configText.find("/default|")]
    default_sample = default_sample.replace("variable", input_text)
    defaultPart = default_sample


def text_color(color):
    global coloredPart, configText

    if color != 'nothing':
        default_sample = configText[configText.find("|color|")+7:configText.find("/color|")]
        default_sample = default_sample.replace("colorvar", color)
        coloredPart = default_sample
    else:
        pass


def text_outline(outline):
    global outlinePart, configText

    if outline != 'nothing':
        default_sample = configText[configText.find("|outline|")+9:configText.find("/outline|")-1]
        default_sample = default_sample.replace("value", outline)
        outlinePart = default_sample
    else:
        pass


def click_event(event):
    global eventPart, configText

    if event != '':
        default_sample = configText[configText.find("|event|")+7:configText.find("/event|")-1]
        default_sample = default_sample.replace("yourcommand", event)
        eventPart = default_sample
    else:
        pass


def text_maker(input_text, color, outline, event):
    default(input_text)
    text_color(color)
    text_outline(outline)
    click_event(event)
    return defaultPart + coloredPart + outlinePart + eventPart + '}"'
