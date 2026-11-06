import os
import random
n = random.randint(1,10)
guess = input("saisir un nombre ")
guess = int(guess)
if n == guess:
     print(" bien  ")
else:
     print('non pas correct')