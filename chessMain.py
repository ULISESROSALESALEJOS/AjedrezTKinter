import tkinter as tk
from tkinter import Button
from chessController import gameState
import tkinter.dnd as tkd

PANTALLA = tk.Tk()

class App():
    def __init__(self,L_CUADRADO):
        #Aqui accedimos a la clase de la otra hoja
        #self.gd = chessController.gameState()
        self.gs = gameState()
        #self.validarPieza = chessController.gameState.validarPieza(self.primeraJugada)
        
        self.L_CUADRADO = L_CUADRADO
        self.imagenes = {}
        
        self.ventana = PANTALLA
        PANTALLA.bind("<Button-1>", self.primeraJugada)
        self.pieza = ''
        #self.otro_click = False
        
        self.ventana.title("Chess Legend")
        self.ventana.iconbitmap("chess_icon.ico")
        
        #PARA DEFINIR LA DIMENSIÓN DE LA VENTANA
        self.ventana.geometry(f"{str(L_CUADRADO * 8)}x{str(L_CUADRADO*8)}")
        #PARA QUE NO SE EXPANDA MAS DE LO DEFINIDO
        self.ventana.resizable(0,0)

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        
    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO,j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO,j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#7a4f37")
                    
    def loadImg(self):
        piezas = ["np","nT","nC","nA","nD","nR","bp","bT","bC","bA","bD","bR"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./img/"+ pieza + ".png")
                    
    def showPiezas(self):
        #indice_i rescata la fila, i guardara la lista entera de esa fila
        for indice_i,i in enumerate(self.gs.piezas):
            #Aqui enumeramos de 'i' ya que es la que guarda la lista de la fila anterior seleccionada
            for indice_j,j in enumerate(i):
                if j != "--":
                    self.interfaz.create_image(indice_j*self.L_CUADRADO, indice_i*self.L_CUADRADO, image=self.imagenes[j], anchor="nw")
        pass
        
    def primeraJugada(self,event):
        fila = int(event.y / 60)
        columna = int(event.x /60)
        print("---------")
        print("Primer click: ","fila:", fila, ",","columna", columna)
        filaX = self.gs.piezas[fila]
        self.pieza = filaX[columna]
        if self.pieza == 'np':
            self.ventana.wait_variable(self.ventana.bind("<Button-1>", self.segundaJugada))
            
    def segundaJugada(self, event):
        fila = int(event.y / self.L_CUADRADO)
        columna = int(event.x / self.L_CUADRADO)
        filaM = self.gs.piezas[fila]
        #filaM[columna] = self.imagenes[self.pieza]
        if self.pieza in self.imagenes:
            filaM[columna] = self.interfaz.create_image(columna*self.L_CUADRADO, fila*self.L_CUADRADO, image=self.imagenes[self.pieza], anchor="nw")
        else:
            print("No esta")
        print("Segundo click: ","fila:", fila, ",","columna", columna)
        print("---------")
        self.pieza = ''
        self.primeraJugada(event)
        
runChess = App(60)
runChess.dibujarTablero()
runChess.loadImg()
runChess.showPiezas()
runChess()