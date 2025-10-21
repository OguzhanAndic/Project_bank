
import random


def make_hardpass():
    gen_bokstav = ["a", "b", "c", "d", "e", "f" , "g", "h", "j", "k", "l", "m", "n" , "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    gen_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gen_unik = ["#", "@", "!", "£", "%", "&"]
    uniq_code = []

    choice1 = 60
    choice2 = 60
    choice3 = 30
    print(f'Generated code will have the following: {choice1} letters, {choice2} numbers, {choice3} special letters')
    for number in range(1, choice1 + 1):
        uniq_code += random.choice(gen_bokstav)
    for number in range(1, choice2 + 1):
        uniq_code += random.choice(gen_num)
    for number in range(1, choice3 + 1):
        uniq_code += random.choice(gen_unik)

    uniq_password = ""

    for option in range(1, (len(uniq_code)) +1 ):
        temp1 = random.choice(uniq_code)
        uniq_password += temp1 
        uniq_code.remove(temp1)
    
    while True:
        makesure = input("This password generated is a sensetive key and should not be shared with anyone. Do you want to keep this key? Y/N: ")
        if makesure.lower() == "yes" or makesure.lower() == "y" :
            print(f'Your following password: {uniq_password}')
            break
        elif makesure.lower() == "no" or makesure.lower() == "n":
            print(f'Breaking the key')
            break
        else:
            print(f'Not a valid answer, asking again...')

