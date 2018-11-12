#    This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import ttk
import math
root = Tk()
diamondpick = ""
### GLOBALS ###
click=True
### FUNCTIONS ###
global craftedimage
craftedimage = ""
def clearentry():
    faillabel.config(text="Improper inputs, try again.")
    c1.config(text="")
    c2.config(text="")
    c3.config(text="")
    c4.config(text="")
    c5.config(text="")
    c6.config(text="")
    c7.config(text="")
    c8.config(text="")
    c9.config(text="")
    labeltext.set("")
    imagepic.config(image="")
    c1i = PhotoImage(file="blank.png")
    c1.config(image=c1i)
    c1.photo = c1i
    c2i = PhotoImage(file="blank.png")
    c2.config(image=c2i)
    c2.photo = c2i
    c3i = PhotoImage(file="blank.png")
    c3.config(image=c3i)
    c3.photo = c3i
    c4i = PhotoImage(file="blank.png")
    c4.config(image=c4i)
    c4.photo = c4i
    c5i = PhotoImage(file="blank.png")
    c5.config(image=c5i)
    c5.photo = c5i
    c6i = PhotoImage(file="blank.png")
    c6.config(image=c6i)
    c6.photo = c6i
    c7i = PhotoImage(file="blank.png")
    c7.config(image=c7i)
    c7.photo = c7i
    c8i = PhotoImage(file="blank.png")
    c8.config(image=c8i)
    c8.photo = c8i
    c9i = PhotoImage(file="blank.png")
    c9.config(image=c9i)
    c9.photo = c9i
def changebutton(cv):
    c1.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c1i = PhotoImage(file="ironpng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo=c1i
    elif itemselect.get() == "Diamond":
        c1i = PhotoImage(file="diamondpng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo = c1i
    elif itemselect.get() == "Sticks":
        c1i = PhotoImage(file="stickspng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo = c1i
    elif itemselect.get() == "Wooden Planks":
        c1i = PhotoImage(file="signpng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo = c1i
    elif itemselect.get() == "Gold":
        c1i = PhotoImage(file="goldpng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo = c1i
    elif itemselect.get() == "Cobblestone":
        c1i = PhotoImage(file="cobblestonepng.png")
        c1i = c1i.zoom(25)
        c1i = c1i.subsample(32)
        c1.config(image=c1i)
        c1.photo = c1i
    else:
        c1i = PhotoImage(file="blank.png")
        c1.config(image=c1i)
        c1.photo = c1i
def changebutton2(cv):
    c2.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c2i = PhotoImage(file="ironpng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo=c2i
    elif itemselect.get() == "Diamond":
        c2i = PhotoImage(file="diamondpng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo = c2i
    elif itemselect.get() == "Sticks":
        c2i = PhotoImage(file="stickspng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo = c2i
    elif itemselect.get() == "Wooden Planks":
        c2i = PhotoImage(file="signpng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo = c2i
    elif itemselect.get() == "Gold":
        c2i = PhotoImage(file="goldpng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo = c2i
    elif itemselect.get() == "Cobblestone":
        c2i = PhotoImage(file="cobblestonepng.png")
        c2i = c2i.zoom(25)
        c2i = c2i.subsample(32)
        c2.config(image=c2i)
        c2.photo = c2i
    else:
        c2i = PhotoImage(file="blank.png")
        c2.config(image=c2i)
        c2.photo = c2i
def changebutton3(cv):
    c3.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c3i = PhotoImage(file="ironpng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo=c3i
    elif itemselect.get() == "Diamond":
        c3i = PhotoImage(file="diamondpng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo = c3i
    elif itemselect.get() == "Sticks":
        c3i = PhotoImage(file="stickspng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo = c3i
    elif itemselect.get() == "Wooden Planks":
        c3i = PhotoImage(file="signpng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo = c3i
    elif itemselect.get() == "Gold":
        c3i = PhotoImage(file="goldpng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo = c3i
    elif itemselect.get() == "Cobblestone":
        c3i = PhotoImage(file="cobblestonepng.png")
        c3i = c3i.zoom(25)
        c3i = c3i.subsample(32)
        c3.config(image=c3i)
        c3.photo = c3i
    else:
        c3i = PhotoImage(file="blank.png")
        c3.config(image=c3i)
        c3.photo = c3i
def changebutton4(cv):
    c4.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c4i = PhotoImage(file="ironpng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo=c4i
    elif itemselect.get() == "Diamond":
        c4i = PhotoImage(file="diamondpng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo = c4i
    elif itemselect.get() == "Sticks":
        c4i = PhotoImage(file="stickspng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo = c4i
    elif itemselect.get() == "Wooden Planks":
        c4i = PhotoImage(file="signpng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo = c4i
    elif itemselect.get() == "Gold":
        c4i = PhotoImage(file="goldpng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo = c4i
    elif itemselect.get() == "Cobblestone":
        c4i = PhotoImage(file="cobblestonepng.png")
        c4i = c4i.zoom(25)
        c4i = c4i.subsample(32)
        c4.config(image=c4i)
        c4.photo = c4i
    else:
        c4i = PhotoImage(file="blank.png")
        c4.config(image=c4i)
        c4.photo = c4i
def changebutton5(cv):
    c5.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c5i = PhotoImage(file="ironpng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo=c5i
    elif itemselect.get() == "Diamond":
        c5i = PhotoImage(file="diamondpng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo = c5i
    elif itemselect.get() == "Sticks":
        c5i = PhotoImage(file="stickspng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo = c5i
    elif itemselect.get() == "Wooden Planks":
        c5i = PhotoImage(file="signpng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo = c5i
    elif itemselect.get() == "Gold":
        c5i = PhotoImage(file="goldpng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo = c5i
    elif itemselect.get() == "Cobblestone":
        c5i = PhotoImage(file="cobblestonepng.png")
        c5i = c5i.zoom(25)
        c5i = c5i.subsample(32)
        c5.config(image=c5i)
        c5.photo = c5i
    else:
        c5i = PhotoImage(file="blank.png")
        c5.config(image=c5i)
        c5.photo = c5i
def changebutton6(cv):
    c6.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c6i = PhotoImage(file="ironpng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo=c6i
    elif itemselect.get() == "Diamond":
        c6i = PhotoImage(file="diamondpng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo = c6i
    elif itemselect.get() == "Sticks":
        c6i = PhotoImage(file="stickspng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo = c6i
    elif itemselect.get() == "Wooden Planks":
        c6i = PhotoImage(file="signpng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo = c6i
    elif itemselect.get() == "Gold":
        c6i = PhotoImage(file="goldpng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo = c6i
    elif itemselect.get() == "Cobblestone":
        c6i = PhotoImage(file="cobblestonepng.png")
        c6i = c6i.zoom(25)
        c6i = c6i.subsample(32)
        c6.config(image=c6i)
        c6.photo = c6i
    else:
        c6i = PhotoImage(file="blank.png")
        c6.config(image=c6i)
        c6.photo = c6i
def changebutton7(cv):
    c7.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c7i = PhotoImage(file="ironpng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo=c7i
    elif itemselect.get() == "Diamond":
        c7i = PhotoImage(file="diamondpng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo = c7i
    elif itemselect.get() == "Sticks":
        c7i = PhotoImage(file="stickspng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo = c7i
    elif itemselect.get() == "Wooden Planks":
        c7i = PhotoImage(file="signpng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo = c7i
    elif itemselect.get() == "Gold":
        c7i = PhotoImage(file="goldpng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo = c7i
    elif itemselect.get() == "Cobblestone":
        c7i = PhotoImage(file="cobblestonepng.png")
        c7i = c7i.zoom(25)
        c7i = c7i.subsample(32)
        c7.config(image=c7i)
        c7.photo = c7i
    else:
        c7i = PhotoImage(file="blank.png")
        c7.config(image=c7i)
        c7.photo = c7i
def changebutton8(cv):
    c8.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c8i = PhotoImage(file="ironpng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo=c8i
    elif itemselect.get() == "Diamond":
        c8i = PhotoImage(file="diamondpng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo = c8i
    elif itemselect.get() == "Sticks":
        c8i = PhotoImage(file="stickspng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo = c8i
    elif itemselect.get() == "Wooden Planks":
        c8i = PhotoImage(file="signpng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo = c8i
    elif itemselect.get() == "Gold":
        c8i = PhotoImage(file="goldpng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo = c8i
    elif itemselect.get() == "Cobblestone":
        c8i = PhotoImage(file="cobblestonepng.png")
        c8i = c8i.zoom(25)
        c8i = c8i.subsample(32)
        c8.config(image=c8i)
        c8.photo = c8i
    else:
        c8i = PhotoImage(file="blank.png")
        c8.config(image=c8i)
        c8.photo = c8i
def changebutton9(cv):
    c9.config(text=itemselect.get())
    if itemselect.get() == "Iron":
        c9i = PhotoImage(file="ironpng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo=c9i
    elif itemselect.get() == "Diamond":
        c9i = PhotoImage(file="diamondpng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo = c9i
    elif itemselect.get() == "Sticks":
        c9i = PhotoImage(file="stickspng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo = c9i
    elif itemselect.get() == "Wooden Planks":
        c9i = PhotoImage(file="signpng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo = c9i
    elif itemselect.get() == "Gold":
        c9i = PhotoImage(file="goldpng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo = c9i
    elif itemselect.get() == "Cobblestone":
        c9i = PhotoImage(file="cobblestonepng.png")
        c9i = c9i.zoom(25)
        c9i = c9i.subsample(32)
        c9.config(image=c9i)
        c9.photo = c9i
    else:
        c9i = PhotoImage(file="blank.png")
        c9.config(image=c9i)
        c9.photo = c9i
def insitem():
    pass
    showPosEvent(event)
def updatelabel(x):
    labeltext.set(x)
def craft():
    faillabel.config(text="")
    global c1v
    global c2v
    global c3v
    global c4v
    global c5v
    global c6v
    global c7v
    global c8v
    global c9v
    global craftedimage
    box1=(c1.config("text")[-1])
    box2=(c2.config("text")[-1])
    box3=(c3.config("text")[-1])
    box4=(c4.config("text")[-1])
    box5=(c5.config("text")[-1])
    box6=(c6.config("text")[-1])
    box7=(c7.config("text")[-1])
    box8=(c8.config("text")[-1])
    box9=(c9.config("text")[-1])
    if box1 == "Wooden Planks" and box2 == "Wooden Planks" and box3 == "Wooden Planks" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("wooden pickaxe!")
        craftedimage = PhotoImage(file="woodpickpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Cobblestone" and box2 == "Cobblestone" and box3 == "Cobblestone" and box5 == "Sticks" and box8 == "Sticks" and box4 == "" and box6 == "" and box7 == "" and box9 == "":
        updatelabel("stone pickaxe!")
        craftedimage = PhotoImage(file="stonepickpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Iron" and box2 == "Iron" and box3 == "Iron" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("iron pickaxe!")
        craftedimage = PhotoImage(file="ironpickpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Diamond" and box2 == "Diamond" and box3 == "Diamond" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("diamond pickaxe!")
        craftedimage = PhotoImage(file="diamondpickpng.png") #DIAMOND PICK
        imagepic.config(image=craftedimage)
    elif box1 == "Gold" and box2 == "Gold" and box3 == "Gold" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("gold pickaxe!")
        craftedimage = PhotoImage(file="goldpick.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Wooden Planks" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("wooden shovel!")
        craftedimage = PhotoImage(file="woodshovelpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Cobblestone" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("stone shovel!")
        craftedimage = PhotoImage(file="stoneshovelpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Iron" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("iron shovel!")
        craftedimage = PhotoImage(file="ironshovelpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Diamond" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("diamond shovel!")
        craftedimage = PhotoImage(file="diamondshovelpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Gold" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("golden shovel!")
        craftedimage = PhotoImage(file="goldenshovelpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Cobblestone" and box2 == "Cobblestone" and box3 == "Cobblestone" and box4== "Cobblestone" and box5 == "" and box6 == "Cobblestone" and box7 == "Cobblestone" and box8 == "Cobblestone" and box9 == "Cobblestone":
        updatelabel("furnace!")
        craftedimage = PhotoImage(file="furnacepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Wooden Planks" and box2 == "Wooden Planks" and box3 == "Wooden Planks" and box4== "Wooden Planks" and box5 == "" and box6 == "Wooden Planks" and box7 == "Wooden Planks" and box8 == "Wooden Planks" and box9 == "Wooden Planks":
        updatelabel("chest!")
        craftedimage = PhotoImage(file="chestpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Wooden Planks" and box3 == "" and box4== "" and box5 == "Wooden Planks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("wooden sword!")
        craftedimage = PhotoImage(file="woodswordpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Cobblestone" and box3 == "" and box4== "" and box5 == "Cobblestone" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("stone sword!")
        craftedimage = PhotoImage(file="stoneswordpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Iron" and box3 == "" and box4== "" and box5 == "Iron" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("iron sword!")
        craftedimage = PhotoImage(file="ironswordpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Diamond" and box3 == "" and box4== "" and box5 == "Diamond" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("diamond sword!")
        craftedimage = PhotoImage(file="diamondswordpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "" and box2 == "Gold" and box3 == "" and box4== "" and box5 == "Gold" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("golden sword!")
        craftedimage = PhotoImage(file="enwordpng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Wooden Planks" and box2 == "Wooden Planks" and box3 == "" and box4== "Wooden Planks" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("wooden axe!")
        craftedimage = PhotoImage(file="woodaxepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Cobblestone" and box2 == "Cobblestone" and box3 == "" and box4== "Cobblestone" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("stone axe!")
        craftedimage = PhotoImage(file="stoneaxepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Iron" and box2 == "Iron" and box3 == "" and box4== "Iron" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("iron axe!")
        craftedimage = PhotoImage(file="ironaxepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Diamond" and box2 == "Diamond" and box3 == "" and box4== "Diamond" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("diamond axe!")
        craftedimage = PhotoImage(file="diamondaxepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Gold" and box2 == "Gold" and box3 == "" and box4== "Gold" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("golden axe!")
        craftedimage = PhotoImage(file="goldaxepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Wooden Planks" and box2 == "Wooden Planks" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("wooden hoe!")
        craftedimage = PhotoImage(file="woodhoepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Cobblestone" and box2 == "Cobblestone" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("stone hoe!")
        craftedimage = PhotoImage(file="stonehoepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Iron" and box2 == "Iron" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("iron hoe!")
        craftedimage = PhotoImage(file="ironhoepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Diamond" and box2 == "Diamond" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("diamond hoe!")
        craftedimage = PhotoImage(file="diamondhoepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Gold" and box2 == "Gold" and box3 == "" and box4== "" and box5 == "Sticks" and box6 == "" and box7 == "" and box8 == "Sticks" and box9 == "":
        updatelabel("golden hoe!")
        craftedimage = PhotoImage(file="goldhoepng.png")
        imagepic.config(image=craftedimage)
    elif box1 == "Wooden Planks" and box2 == "" and box3 == "" and box4== "" and box5 == "Wooden Planks" and box6 == "" and box7 == "" and box8 == "" and box9 == "":
        updatelabel("sticks!")
        craftedimage = PhotoImage(file="stickspng.png")
        imagepic.config(image=craftedimage)
    else:
        clearentry()

### CRAFTING SELECTION AND CRAFT/CLEAR BUTTONS ###
items = ["", "Wooden Planks", "Cobblestone", "Iron", "Gold", "Diamond", "Sticks"]
itemselect = ttk.Combobox(root, height=16, width=16, value=items, state="readonly")
itemselect.grid(row=0, column=0, sticky=NSEW, ipady="1")
unneccessarylabel = Label(text="You crafted a(n): ")
unneccessarylabel.grid(row=1, column=0, sticky="w")
labeltext=StringVar()
newitem = Label(textvariable=labeltext)
labeltext.set("")
newitem.grid(row=2, column=0, sticky="s")
imagepic=Label(image=craftedimage)
imagepic.grid(row=3, column=0, sticky="n")
submit=Button(text="Craft", command=craft)
submit.grid(row=0, column=9, sticky="nsew")
clear=Button(text="Clear", command=clearentry)
clear.grid(row=1, column=9, sticky="nsew")
xy=StringVar()
xy.set("")
faillabel = Label(text="")
faillabel.grid(row=4, column=0)
### 3X3 CRAFTING MENU ###
crafting = Frame()
c1v=""
c2v=""
c3v=""
c4v=""
c5v=""
c6v=""
c7v=""
c8v=""
c9v=""
c1i = PhotoImage(file="blank.png")
c2i = PhotoImage(file="blank.png")
c3i = PhotoImage(file="blank.png")
c4i = PhotoImage(file="blank.png")
c5i = PhotoImage(file="blank.png")
c6i = PhotoImage(file="blank.png")
c7i = PhotoImage(file="blank.png")
c8i = PhotoImage(file="blank.png")
c9i = PhotoImage(file="blank.png")
c1=Button(crafting, textvariable=c1v, relief="raised", image=c1i, command=lambda:changebutton(c1v))
c1.grid(row=2, column=6)
c2=Button(crafting, textvariable=c2v, relief="raised", image=c2i, command=lambda:changebutton2(c2v))
c2.grid(row=2, column=7)
c3=Button(crafting, textvariable=c3v, relief="raised", image=c3i, command=lambda:changebutton3(c3v))
c3.grid(row=2, column=8)
c4=Button(crafting, textvariable=c4v, relief="raised", image=c4i, command=lambda:changebutton4(c4v))
c4.grid(row=3, column=6)
c5=Button(crafting, textvariable=c5v, relief="raised", image=c5i, command=lambda:changebutton5(c5v))
c5.grid(row=3, column=7)
c6=Button(crafting, textvariable=c6v, relief="raised", image=c6i, command=lambda:changebutton6(c6v))
c6.grid(row=3, column=8)
c7=Button(crafting, textvariable=c7v, relief="raised", image=c7i, command=lambda:changebutton7(c7v))
c7.grid(row=4, column=6)
c8=Button(crafting, textvariable=c8v, relief="raised", image=c8i, command=lambda:changebutton8(c8v))
c8.grid(row=4, column=7)
c9=Button(crafting, textvariable=c9v, relief="raised", image=c9i, command=lambda:changebutton9(c9v))
c9.grid(row=4, column=8)
crafting.grid(row=0, column=6, rowspan=9999, sticky=NSEW)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.columnconfigure(9, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.title("Minecraft Crafting")
root.geometry("427x218")
root.mainloop()