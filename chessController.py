import tkinter as tk
import tkinter.dnd as tkd
from tkinter import Button

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

    def validarPieza(self,pieza):
        print(f"Estoy reconociendo desde la otra hoja:{pieza}")
        pass

    def validar(self):
        print("Hoal desde aqui")
        
        
    
    def moverPieza(self):
        pass
    

    
    