# password Generator
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import string
import random
# genrating a function first
def genrate_pass_random(length):
    character=string.ascii_letters + string.digits + string.punctuation
    random_string=''.join(random.choices(character, k=length))
    return random_string
# taking choices of users
user_input=int(input("length of pass must be---->"))
random_str=genrate_pass_random(user_input)
print("the highly protected and newly genrated pass is",random_str)

       
    


