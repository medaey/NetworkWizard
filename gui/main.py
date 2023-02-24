from tkinter import *
from tkinter import ttk
from route_tab import RouteTab

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self.master)

        # Ajout des onglets
        for tab_class in [RouteTab]:
            tab = tab_class(notebook)
            notebook.add(tab, text=tab.label)

        notebook.pack()

root = Tk()
app = Application(master=root)
app.mainloop()