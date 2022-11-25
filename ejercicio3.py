import pandas as pd
import numpy as np

datos = {"Nombre":["Petra","Taj Mahal", "Machu Picchu", "Pirámide de Chichén Itzá", "Coliseo de Roma", "Gran Muralla China", "Cristo Redentor"], "Ubicación":["Jordania", "India", "Perú", "Yucatán", "Roma", " China", "Brasil"], "Tipo":["Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura"]}

class Grafo:
    def __init__(self):