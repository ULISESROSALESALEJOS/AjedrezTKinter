import tkinter as tk

class gameState():
    
    #Esto es una función de instancia para autollamarse
    def __init__(self):
        
        self.piezas = [
        ["nT","nC","nA","nD","nR","nA","nC","nT"],
        ["np","np","np","np","np","np","np","np"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["bT","bC","bA","bD","bR","bA","bC","bT"]
        ]
    
class movePieza():
    def add_move(self,widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>",self.on_drag)
        widget.bind("<ButtonRelease-1>",self.on_drop)
        widget.configure(cursor="hand1")
        
    def on_start(self, event):
        pass
    def on_drag(self,event):
        pass
    def on_drop(self,event):
        x,y = event.move.winfo_pointerxy()
        target = event.move.winfo_containing(x,y)
        try:
            target.configure(image=event.move.cget("img/*"))
        except:
            pass
    