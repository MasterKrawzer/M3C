import converter as main
from Tkinter import *

root = Tk()

text = Text(root, height=1)
text.insert(INSERT, main.textmaker("lol", "blue", "italic", "N"))
text.pack(anchor=CENTER)

root.mainloop()

