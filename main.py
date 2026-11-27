from models import coches_models
from view.coches_view import CochesView
import tkinter as tk
from tkinter import Tk
 
class App:
    def __init__(self, ventana):
        self.ventana = ventana
        CochesView(self.ventana)
if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()