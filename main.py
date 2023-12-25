import random

import enda

should_continue = True
while should_continue:
    print("Welcome to my password generator!")

    num_norm_let = int(input("\nHow many normal_letters do you want ? "))
    normal_letters = random.sample(enda.normal_letters, k=num_norm_let)

    num_cap_let = int(input("How many capital_letters do you want ? "))
    capital_letters = random.sample(enda.capital_letters, k=num_cap_let)

    num_num = int(input("How many numbers do you want ? "))
    digits = random.sample(enda.digits, k=num_num)

    spe_numbness = int(input("How many special symbols do you want to be in the password ? "))
    special_symbols = random.sample(enda.special_symbols, k=spe_numbness)

    combination = normal_letters + capital_letters + digits + special_symbols

    code = random.sample(combination, k=len(combination))

    password = ""
    for char in code:
        password += char

    print(f"\nYour password is:\n{password}")

    continuation = input("\nDo you want to continue work with password generator ? Type 'yes' or 'no': ").lower()
    if continuation == "no":
        should_continue = False
