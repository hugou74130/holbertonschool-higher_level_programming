#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements# Affecte une valeur à 'common_elements'

set_1 = { "Python", "C", "Javascript" }# Affecte une valeur à 'set_1'
set_2 = { "Bash", "C", "Ruby", "Perl" }# Affecte une valeur à 'set_2'
c_set = common_elements(set_1, set_2)# Affecte une valeur à 'c_set'
print(sorted(list(c_set)))# Affiche à l'écran
