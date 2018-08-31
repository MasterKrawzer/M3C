import text_gui as text
from Tkinter import *

root = Tk()
root.title("M3C")


########################################
def totext():
    text.start()


########################################
Button(root, text="Text compiler", command=totext).pack()
########################################
root.mainloop()
