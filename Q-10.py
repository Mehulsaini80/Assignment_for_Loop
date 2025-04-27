# 10.Write a program to enter a number and print its reverse.
n=int(input("Enter a number: "));

rev=0
while(n!=0):
    rem=n%10;
    rev=rev*10+rem;  
    n=n//10;
    
print(rev);