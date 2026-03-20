#!/usr/bin/python3

import xml.etree.ElementTree as ET # import la librairie xml

def serialize_to_xml(dictionary, filename):# definit serialize_to_xml avec comme argument dictionary et filename
    root = ET.Element("data") # crée l'élément dans la racine data
    for key, value in dictionary.items():# fais une boucle sur key avec la valeur du dictionnaire
        child = ET.SubElement(root,key)# création d'un sous élément enfant avec root comme parent key comme nom de balise
        child.text = str(value)# permet de mettre une string de value dans child.text
    ET.ElementTree(root).write(filename, encoding="utf-8",xml_declaration=True) # écrit l'arbre XML dans le fichier 

def deserialize_from_xml(filename): # définit deserialize_from_xml 

    parse = ET.parse(filename) # parse le fichier filename
    root = parse.getroot() # parse le root 
    return {child.tag: child.text for child in root} # retourne un dictionnaire avec les nom de balises comme cles et leur cintenu comme valeurs 