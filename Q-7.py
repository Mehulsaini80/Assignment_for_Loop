# 7. Write a program to calculate the sum of digits of a number.
n=int(input("Enter a number: "))

sum=0
for i in range(0,n):
    rem=n%10;  #123 3
    sum=sum+rem;  #3
    n=n//10;  #12 
print(sum)