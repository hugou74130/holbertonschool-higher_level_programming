#/usr/bin/python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""

import json #Module d'importation json essentielle pour les commande suivante 


def serialize_and_save_to_file(data, filename): # Je définie et je donne comme argument date et file name
    with open(filename,'w', encoding= "utf-8") as file: # J'ouvre le fichier en mode ecriture avec un enconding utf 8
        json.dump(data, file) # Je dump le fichier json avec les argument de data et file
    

def load_and_deserialize(filename):
    with open(filename, 'r', encoding="utf-8") as file: #J'ouvre le fichier en mode lecture avec un lencoding utf 8
       return json.load(file) #Je retourne le json avec comme argument file 
