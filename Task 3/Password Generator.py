import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter the length of the password: "))

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Generated Password:", password)