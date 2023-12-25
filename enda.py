import random

normal_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "=", "?", "@"]

len_pas = int(input("How long do you want your password to be ? "))

num_norm_lett = int(input("How many normal_letters do you want ? "))
normal_letters = random.sample(normal_letters, k=num_norm_lett)

num_cap_lett = int(input("How many capital_letters do you want ? "))
capital_letters = random.sample(capital_letters, k=num_cap_lett)

num_num = int(input("How many numbers do you want ? "))
digits = random.sample(digits, k=num_num)

spe_numbness = int(input("How many special symbols do you want to be in the password ? "))
special_symbols = random.sample(special_symbols, k=spe_numbness)
