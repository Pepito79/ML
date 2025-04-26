import pandas as pd
import json
from fichier import tickets


def json_list(tickets):
    l = []
    for t in tickets:
        try:
            data = json.loads(t)  # Chargement du JSON
            l.append(data)  # Ajoute l'objet Python dans la liste
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON : {e}")
    return l

def insert_df (liste):
    df = pd.DataFrame()
    for elem in liste:
        arcticles = elem["articles"]
        