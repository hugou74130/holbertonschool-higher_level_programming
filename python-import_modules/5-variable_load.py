#!/usr/bin/python3

# Script démontrant le chargement d'une variable depuis un module externe
if __name__ == "__main__":  # Condition si exécuté en tant que script
    from variable_load_5 import a  # Importe la variable 'a' depuis le module 'variable_load_5'

    # Affiche la valeur importée
    print(a)  # Affiche à l'écran