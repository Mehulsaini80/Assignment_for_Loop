#11.Write a program to find the power of a number using for loop.

num=int(input("Enter number: "))
power=int(input("Enter power: "))

p=1
for i in range(0,power):
    p=p*num
    
print("Answer:",p);
    
    