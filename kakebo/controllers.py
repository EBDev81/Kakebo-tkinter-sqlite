import tkinter as tk
from kakebo.vistas import FormMovimiento, ListaMovimientos
from kakebo.modelos import DaoSqlite
from kakebo import PATH_DATABASE

class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kakebo")
        self.lista = ListaMovimientos(self)
        self.lista.pack()
        self.form = FormMovimiento(self, self.grabaMovimiento)
        self.form.pack()
        self.dao = DaoSqlite(PATH_DATABASE)

    def grabaMovimiento(self, movimiento):
        self.dao.grabar(movimiento)
    
        