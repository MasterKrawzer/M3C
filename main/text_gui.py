from Tkinter import *
import clipboard
import time
import text as main
########################################

colors = [
    "nothing",
    "black",
    "dark_blue",
    "dark_green",
    "dark_aqua",
    "dark_red",
    "gold",
    "gray",
    "dark_gray",
    "blue",
    "green",
    "aqua",
    "red",
    "light_purple",
    "yellow",
    "white"
]

outlines = [
    "nothing",
    "bold",
    "italic",
    "strikethrow",
    "underline",
    "obfuscated"
]
########################################


def start():
    textconverter = Tk()
    textconverter.title("Text Compiler")

    ########################################
    txt = StringVar(textconverter)
    color = StringVar(textconverter)
    outline = StringVar(textconverter)
    command = StringVar(textconverter)

    ########################################
    def confirm():
        clipboard.copy("")
        clipboard.copy(main.textmaker(txt, color, outline, command))

    ########################################
    Label(textconverter, text="Text").grid(row=0, sticky=W)
    text = Entry(textconverter, textvariable=txt, width=50)
    text.grid(row=0, column=1)

    ########################################
    Label(textconverter, text="Color").grid(row=1, sticky=W)
    OptionMenu(textconverter, color, *colors).grid(row=1, column=1, sticky=W + E)
    color.set(colors[0])

    ########################################
    Label(textconverter, text="Options").grid(row=2, sticky=W)
    OptionMenu(textconverter, outline, *outlines).grid(row=2, column=1, sticky=W + E)
    outline.set(outlines[0])

    ########################################
    Label(textconverter, text="Command").grid(row=3, sticky=W)
    commandLine = Entry(textconverter, textvariable=command, width=50)
    commandLine.grid(row=3, column=1)

    ########################################
    Button(textconverter, text="Confirm", command=confirm).grid(row=4)

    ########################################
    Entry(textconverter, textvariable=result, width=50).grid(row=5, columnspan=2, sticky=W + E)

    ########################################
    textconverter.mainloop()