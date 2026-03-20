#!/usr/bin/python3

import csv # importe la librairie csv
import json # imorte la librairie json


def convert_csv_to_json(csv_filename): # definitie cincert_csv_to_json avec comme argument csv_filename
    try: # essaie
        with open(csv_filename, "r", encoding="utf-8") as csvfile: # ouverture du fichier csv_filename en mode read avec lenconding utf-8
            reader = csv.DictReader(csvfile) # cree un lecteur csv qui retourne des dictionnaire 
            rows = [row for row in reader] # permet de lire chaque ligne du fichier grace a rows
        with open("data.json", "w", encoding="utf-8") as jsonfile: # ouvre le fichier data.json en mode ecriture avec lencoding utf-8 
            json.dump(rows, jsonfile, indent=4) # sérialise le fichier avec comme argument rows et le json file et une indentation d'une valeur de 4
        return True # retourne vrais si tout est bon
    except FileNotFoundError: # leve une exception dune erreur 
        return False # retourne le programme en tant que faux 
    except Exception: # leve une exception
        return False # retourne le programme en tant que faux
