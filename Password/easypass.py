import random


def make_easypass():
    gen_bokstav = ["a", "b", "c", "d", "e", "f" , "g", "h", "j", "k", "l", "m", "n" , "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    gen_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gen_unik = ["#", "@", "!", "£", "%", "&"]
    uniq_code = []

    choice1 = 10
    choice2 = 10
    choice3 = 5
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
    print(f'Your following password: {uniq_password}')
