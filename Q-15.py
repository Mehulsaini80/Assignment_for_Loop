#15.Write a program to check whether a number is Prime number or not.

num=int(input("Enter a number: "))

count=0
for i in range(2,num):
    if(num%i==0):
        count+=1
        
if(count>0):
    print("Not Prime")
else:
    print("Prime");
        