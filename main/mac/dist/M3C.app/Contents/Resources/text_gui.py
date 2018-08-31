from Tkinter import *
from threading import Timer
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
    text_converter = Tk()
    text_converter.title("Text Compiler")

    ########################################
    txt = StringVar(text_converter)
    color = StringVar(text_converter)
    outline = StringVar(text_converter)
    command = StringVar(text_converter)
    result = StringVar(text_converter)

    ########################################
    def timer():
        result.set("")
        t = Timer(2, timer)
        t.start()

    t = Timer(2, timer)
    t.start()

    ########################################
    result.set("Waiting for orders...")

    ########################################
    def confirm():
        text_converter.clipboard_clear()
        text_converter.clipboard_append(main.textmaker(txt.get(), color.get(), outline.get(), command.get()))
        text_converter.update()
        result.set("Added to the clipboard!")
        t.start()

    ########################################
    Label(text_converter, text="Text").grid(row=0, sticky=W)
    text = Entry(text_converter, textvariable=txt, width=50)
    text.grid(row=0, column=1)

    ########################################
    Label(text_converter, text="Color").grid(row=1, sticky=W)
    OptionMenu(text_converter, color, *colors).grid(row=1, column=1, sticky=W + E)
    color.set(colors[0])

    ########################################
    Label(text_converter, text="Options").grid(row=2, sticky=W)
    OptionMenu(text_converter, outline, *outlines).grid(row=2, column=1, sticky=W + E)
    outline.set(outlines[0])

    ########################################
    Label(text_converter, text="Command").grid(row=3, sticky=W)
    command_line = Entry(text_converter, textvariable=command, width=50)
    command_line.grid(row=3, column=1)

    ########################################
    Button(text_converter, text="Confirm", command=confirm).grid(row=4, columnspan=2)

    ########################################
    Label(text_converter, textvariable=result, width=23).grid(row=5, columnspan=2)

    ########################################
    text_converter.mainloop()
