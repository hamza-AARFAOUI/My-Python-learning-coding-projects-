import random
def number():
    a=random.randint(1,10)
    num=None
    print("voulez vous deviner un nombre caché ")
    i=0
    while a!=num   and i<3 :
        i=i+1
        num=int(input("choisir un nombre entre 1et 10:"))

        if  a==num:
           print("perfect")
        elif num<a:
           print("your guess is lower")

        elif num>a :
           print("your guess is high")

number()