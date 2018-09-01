from Tkinter import *
########################################


def start():
    root = Tk()
    root.title("Chest prefiller")


    #     When slot selected:
    def selected(event, frame):
        frame.configure(bg="yellow")


    #     When slot deselected:
    def deselected(event, frame):
        frame.configure(bg="white")


    # Frame init &
    # **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &1
    slot1 = Frame(root, width=50, height=50)
    slot1.bind("<Enter>", lambda event: selected(event, slot1))
    slot1.bind("<Leave>", lambda event: deselected(event, slot1))
    slot1.grid(row=0, column=1)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &2
    slot2 = Frame(root, width=50, height=50)
    slot2.bind("<Enter>", lambda event: selected(event, slot2))
    slot2.bind("<Leave>", lambda event: deselected(event, slot2))
    slot2.grid(row=0, column=2)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &3
    slot3 = Frame(root, width=50, height=50)
    slot3.bind("<Enter>", lambda event: selected(event, slot3))
    slot3.bind("<Leave>", lambda event: deselected(event, slot3))
    slot3.grid(row=0, column=3)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &4
    slot4 = Frame(root, width=50, height=50)
    slot4.bind("<Enter>", lambda event: selected(event, slot4))
    slot4.bind("<Leave>", lambda event: deselected(event, slot4))
    slot4.grid(row=0, column=4)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &5
    slot5 = Frame(root, width=50, height=50)
    slot5.bind("<Enter>", lambda event: selected(event, slot5))
    slot5.bind("<Leave>", lambda event: deselected(event, slot5))
    slot5.grid(row=0, column=5)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &6
    slot6 = Frame(root, width=50, height=50)
    slot6.bind("<Enter>", lambda event: selected(event, slot6))
    slot6.bind("<Leave>", lambda event: deselected(event, slot6))
    slot6.grid(row=0, column=6)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &7
    slot7 = Frame(root, width=50, height=50)
    slot7.bind("<Enter>", lambda event: selected(event, slot7))
    slot7.bind("<Leave>", lambda event: deselected(event, slot7))
    slot7.grid(row=0, column=7)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &8
    slot8 = Frame(root, width=50, height=50)
    slot8.bind("<Enter>", lambda event: selected(event, slot8))
    slot8.bind("<Leave>", lambda event: deselected(event, slot8))
    slot8.grid(row=0, column=8)
    # ()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()^_^()     &9
    slot9 = Frame(root, width=50, height=50)
    slot9.bind("<Enter>", lambda event: selected(event, slot9))
    slot9.bind("<Leave>", lambda event: deselected(event, slot9))
    slot9.grid(row=0, column=9)
    # **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**
    root.mainloop()
