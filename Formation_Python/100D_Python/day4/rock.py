import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]
choice = int(input("What do you choose, 0 = rock, 1 = paper, 2 = scissors ??\n"))
print("User choice:")
if choice >= 3 or choice < 0 :
  print("You taped a invalid number.")
else:
  print(game_image[choice])


random_choice = random.randint(0, 2)
print("Computer choice")
print(game_image[random_choice])

if choice >= 3 or choice < 0 :
   print("You taped an invalid number , you lose ")
elif choice == random_choice :
  print("It's a Draw !")
elif choice == 2 and random_choice == 0:
  print("You lose ")
elif choice == 0 and random_choice == 2:
  print("You win !")
elif choice > random_choice :
  print("You win")
elif choice < random_choice :
  print("You lose")

 