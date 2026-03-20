#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace# Affecte une valeur à 'search_replace'

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]# Affecte une valeur à 'my_list'
new_list = search_replace(my_list, 2, 89)# Affecte une valeur à 'new_list'

print(new_list)# Affiche à l'écran
print(my_list)# Affiche à l'écran
