import text_gui as text
from Tkinter import *

root = Tk()
root.title("M3C")


########################################
def to_text():
    text.start()


########################################
Button(root, text="Text compiler", command=to_text).pack()
########################################
root.mainloop()
