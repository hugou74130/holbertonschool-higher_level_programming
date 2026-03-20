#!/usr/bin/python3

# Déclare la variable `word` contenant un mot exemple
word = "Holberton"  # Affecte une valeur à 'word'

# Exemples d'utilisation du slicing :
# Trois premiers caractères
word_first_3 = word[:3]  # Affecte une valeur à 'word_first_3'
# Deux derniers caractères
word_last_2 = word[-2:]  # Affecte une valeur à 'word_last_2'
# Tout sauf le premier et le dernier caractère
middle_word = word[1:-1]  # Affecte une valeur à 'middle_word'

# Affiche les résultats formatés
print(f"First 3 letters: {word_first_3}")  # Affiche à l'écran
print(f"Last 2 letters: {word_last_2}")  # Affiche à l'écran
print(f"Middle word: {middle_word}")  # Affiche à l'écran
