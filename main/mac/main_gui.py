# /*|*\_/*|*\_/*|*\_/*|*\_/*|*\
import text_gui as text
import chestgen_gui as chestgen
from AnimatedGif import *
from Tkinter import *
from os import getcwd
# /*|*\_/*|*\_/*|*\_/*|*\_/*|*\
# ------------------------------------
# }*{+}*{=}*{+}*{=}*{+}*{=}*{+}*{
root = Tk()
root.title("M3C")
# }*{+}*{=}*{+}*{=}*{+}*{=}*{+}*{
# ------------------------------------
# [VaR]=[Var]=[VaR]=[Var]=[VaR]=[VaR]
way = getcwd()
# [VaR]=[Var]=[VaR]=[Var]=[VaR]=[VaR]
# ------------------------------------
# [GiF]=[GiF]=[GiF]=[GiF]=[GiF]=[GiF]
mmbg = AnimatedGif(root, way + "/resources/mmbg.gif", 0.01)
mmbg.start()
mmbg.grid(row=0, columnspan=100)
# [GiF]=[GiF]=[GiF]=[GiF]=[GiF]=[GiF]
# ------------------------------------
# [FuNc]=[PrOc]=[FuNc]=[PrOc]=[FuNc]=[PrOc]


# Simple empty proc
def none():
    pass
# ------------------------------------


# Transmission to text converter
def to_text():
    text.start()

# ------------------------------------


# Transmission to chest prefiller
def to_chestgen():
    chestgen.start()


# ------------------------------------
# [FuNc]=[PrOc]=[FuNc]=[PrOc]=[FuNc]=[PrOc]

# MAIN+++MAIN+++MAIN+++MAIN+++MAIN+++MAIN+++MAIN
Button(root, text="Text compiler", command=to_text).grid(row=1, column=0, sticky=W)
Button(root, text="NBT/Data tags", command=none).grid(row=1, column=1, sticky=W)
Button(root, text="Prefilled chest generator", command=to_chestgen).grid(row=1, column=1, sticky=W)
# MAIN+++MAIN+++MAIN+++MAIN+++MAIN+++MAIN+++MAIN

# \0|0/===\0|0/===\0|0/===\0|0/
root.mainloop()
