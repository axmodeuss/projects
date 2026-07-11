import random
import string

def get_pass_length():
    my_input = int(input("Enter the number that will be the lenght of your password : "))
    return my_input

def charlist():
    my_data = string.ascii_letters + string.digits + string.punctuation
    return my_data

length = get_pass_length()
characters = charlist()

password = ""
for i in range(length):
    password = password + random.choice(characters)
    
print(password)
    
