import converter as main
from Tkinter import *

root = Tk()
root.title("M3C")
########################################
txt = StringVar(root)
color = StringVar(root)
outline = StringVar(root)
command = StringVar(root)
result = StringVar(root)

colors = [
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
    "bold",
    "italic",
    "strikethrow",
    "underline",
    "obfuscated"
]
########################################


def confirm():
    global result
    result.set(main.textmaker(text, color, outline, command))


########################################
Label(root, text="Text").grid(row=0, sticky=W)
text = Entry(root, textvariable=txt, width=50)
text.grid(row=0, column=1)
########################################
Label(root, text="Color").grid(row=1, sticky=W)
colorMenu = OptionMenu(root, color, *colors).grid(row=1, column=1, sticky=W+E)
color.set(colors[0])
########################################
Label(root, text="Options").grid(row=2, sticky=W)
optionsMenu = OptionMenu(root, outline, *outlines).grid(row=2, column=1, sticky=W+E)
outline.set(outlines[0])
########################################
Label(root, text="Command").grid(row=3, sticky=W)
commandLine = Entry(root, textvariable=command, width=50)
commandLine.grid(row=3, column=1)
########################################
Button(root, text="Confirm", command=confirm).grid(row=4)
########################################
Entry(root, textvariable=result, width=50).grid(row=5, columnspan=2, sticky=W+E)
########################################
root.mainloop()
