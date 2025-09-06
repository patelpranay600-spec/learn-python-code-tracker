# a program for user to predicting no 
import random
num1=int(input("guess which no it can be between 0-9 no"))
random_int=random.randint(1,10)
print("my guessed no",random_int)
if(random_int==num1):
    
    print("you are right")    
    
if(abs(num1-random_int<3)):
    print(" very close")
if(abs(num1-random_int>4)):
    print(" major diffrence")


        
    