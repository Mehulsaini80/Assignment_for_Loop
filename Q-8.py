# 8. Write a program to find the first and last digit of a number.
n=int(input("Enter a number: "))
temp=n;
temp2=n;

count=0;
while(temp2!=0):
    temp2=temp2//10;
    count=count+1;


for i in range(0,count-1):
    temp=temp//10
    
print("First digit",temp)
    
print("Last digit",n%10)
