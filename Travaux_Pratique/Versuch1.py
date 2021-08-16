qt_retirer = 7
fruit_Stocker = [34, 67, 2, 10, 7, 5, 8, 14]
new_fruit_stocker = [nbr_fruit - qt_retirer for nbr_fruit in fruit_Stocker if nbr_fruit > qt_retirer]
print(new_fruit_stocker)