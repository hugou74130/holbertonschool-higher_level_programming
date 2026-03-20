#!/usr/bin/python3
"""
Docstring for python-serialization.task_01_pickle
"""
import pickle #module pour importer pickle


class CustomObject:#creation de la class customobject
    def __init__(self, name: str, age: int, is_student: bool):#initialisation de name(string), age(int), is_student(bool)
        self.name = name #stock la valeur name dans lattribut self.name
        self.age = age #stock la valeur de age dans lattribut self.age
        self.is_student = is_student #stock la valeur de is_student dans lattibut is_student

    def display(self): # définit display avec pour argument self
        print("Name:", self.name) # affiche la valeur de self.name
        print("Age:", self.age) # affiche la valeur de self.age
        print("Is Student:", self.is_student) # affiche la valeur de is_student

    def serialize(self, filename):#définit serialize avec comme argument self et filename 
        try: #essaie
            with open(filename, "wb") as f: #ouverture du fichier en mode ecriture binaire
                pickle.dump(self, f)# avev pickle je serialize le fichier avec les argument self et f 
        except Exception: # si une exception se produit
            return None # retourne none si lexception est passer

    @classmethod
    def deserialize(cls, filename): # definit deserialize avec largument cls et filename
        try: # essaie 
            with open(filename, "rb") as f: # ouvre le fichier en mode read binaire
                obj = pickle.load(f) # load lobjet avec pickle
                return obj # on retourne lobjet
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):# sinon on affiche les erreur suivante
            return None # et in retourne none 
