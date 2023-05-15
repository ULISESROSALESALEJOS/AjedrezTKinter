from tkinter import *
from PIL import ImageTk, Image
import AjedrezTKinter.chessController as chessController



window = Tk()


def loadImg(self):
        piezas = ["np","nT","nC","nA","nD","nR","bp","bT","bC","bA","bD","bR"]
        for pieza in piezas:
            self.imagenes[pieza] = Tk.PhotoImage(file="./img/"+ pieza + ".png")
            
image1 = Image.open("img/nR.png")
image2 = Image.open("img/nT.png")
img1_tk = ImageTk.PhotoImage(image1)
img2_tk = ImageTk.PhotoImage(image2)
PiezaList = chessController.gameState

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startX + event.y
    widget.place(x=x,y=y)

label = Label(window,image=img1_tk)
label.place(x=0,y=0)

label2 = Label(window,image=img2_tk)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()