import os

setts = []

controlVar = "Y"
defaultPart = ""
coloredPart = ""
boldPart = ""
eventPart = ""
way = os.getcwd()

config = open(way + "/config.cfg")
configText = config.read()


def default():
    global defaultPart, configText
    
    defaultSample = configText[configText.find("|default|")+9:configText.find("/default|")-1]
    defaultSample = defaultSample.replace("variable",inputText)
    defaultPart = defaultSample    


def colored():
    global coloredPart, configText

    if col != 'N':
        defaultSample = configText[configText.find("|color|")+7:configText.find("/color|")-1]
        defaultSample = defaultSample.replace("colorvar", col)
        coloredPart = defaultSample
    

def tupe():
    global boldPart, configText, bold
    
    if bold != 'N':
        if bold.find(',') != 1:
            count = bold.count(',') + 1
            setts = bold.split(',')
            for i in range(count):
                defaultSample = configText[configText.find("|bold|")+5:configText.find("/bold|")-1]
                defaultSample = defaultSample.replace("value", setts[i])
                boldPart += defaultSample
        else:
            defaultSample = configText[configText.find("|bold|")+5:configText.find("/bold|")-1]
            defaultSample = defaultSample.replace("value", bold)
            boldPart = defaultSample


def clickEvent():
    global eventPart, configText, event
    
    if event != 'N':
       defaultSample = configText[configText.find("|event|")+6:configText.find("/event|")-1]
       defaultSample = defaultSample.replace("yourcommand", event)
       eventPart = defaultSample


def check():
    global controlVar
    if controlVar == "Y":
        return True
    if controlVar == "N":
        return False

    
while check() == True:
    inputText = input("Enter the text to transmorm it for commands: ")
    col = input("Color? ('N' to skip) ")
    bold = input("Bold/italic/underlined/strikethrough/obstructed? ('N' to skip) ")
    event = input("Command on click (for signs)? ")
    default()
    colored()
    tupe()
    clickEvent()
    print("\nThere you go: " + defaultPart + coloredPart + boldPart + eventPart + '}"')
    controlVar = input("Wanna continue? (Y/N) ")
else:
    quit




