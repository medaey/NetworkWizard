from tkinter import *
from tkinter import ttk
import route



class RouteTab(ttk.Frame):
    label = "Routage"

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Liste des champs de saisie avec valeurs par défaut
        entries = [
            {
                "label": "Réseau destination",
                "default": "172.16.4.0"
            },
            {
                "label": "CIDR",
                "default": "/22"
            },
            {
                "label": "Adresse IP du prochain routeur",
                "default": "192.168.0.1"
            }
        ]

        # Création des champs de saisie
        self.entry_values = []
        for entry in entries:
            label = ttk.Label(self, text=entry["label"])
            label.pack(side=LEFT, padx=5, pady=5)

            entry_value = StringVar(value=entry["default"])
            entry = ttk.Entry(self, textvariable=entry_value)
            entry.pack(side=LEFT, padx=5, pady=5)

            self.entry_values.append(entry_value)

        # Création du bouton OK
        button = ttk.Button(self, text="OK", command=self.route_static)
        button.pack(side=LEFT, padx=5, pady=5)

    def route_static(self):
        # Récupération des valeurs saisies dans les champs de saisie
        reseauDest, cidr, ipNextRouter = (e.get() for e in self.entry_values)

        # Appel à la fonction route_static avec les arguments correspondants
        route.route_static(reseauDest, cidr, ipNextRouter)