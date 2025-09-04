# a program to have all divisors of a particular no
num=int(input("write a no whose divisor is to be checked "))
lst=int(input("the last limit upto you want it to check"))
for i in range(lst):
    if(i>0):
        result= (i%num==0)
        if(result==True):
            print("one of the no is",i)

        

    i=i+1
    


