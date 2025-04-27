# 5. Write a program to find the sum of all odd numbers between 1 to n.

n=int(input("Enter a number: "))
sum=0;
for i in range(1,n+1):
    if(i%2==1):
        sum=sum+i;
print(sum);