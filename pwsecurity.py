import random

def print_logo():
    print("""
    ░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄░░░█▀▀░█▀▀░█▀▀░█░█░█▀▄░▀█▀░▀█▀░█░█
    ░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█░░░▀▀█░█▀▀░█░░░█░█░█▀▄░░█░░░█░░░█░
    ░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░░░▀░  간단한 비밀번호 생성기.
    """)

print_logo()

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "01234567891012131415161718192021222324252627282930"
symbols = """!@#$%^&*()_+-=~`[]{}|;:,.<>/?""\""""

upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
nums = input("Include digits? (y/n): ").strip().lower() == 'y'
syms = input("Include symbols? (y/n): ").strip().lower() == 'y'

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

if len(all) == 0:
    print("You must select at least one character type.")
else:
    length = int(input("Enter the password length: ").strip())
    amount = int(input("Enter the number of passwords to generate: ").strip())

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)











