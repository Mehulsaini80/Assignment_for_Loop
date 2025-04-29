#13.Write a program to calculate the factorial of a number.

num=int(input("Enter a number: "))

fact=1

for i in range(2,num+1):
    fact=fact*i;
print(fact);