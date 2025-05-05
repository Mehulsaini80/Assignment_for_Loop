# 18.Write a program to check whether a number is an Armstrong number or
# not.
# a. An Armstrong number is a n-digit number that is equal to the sum
# of the nth power of its digits. For example –
# 6 = 61 = 6
# 371 = 33 + 73 + 13 = 371

num=int(input("Enter a number: ")) 
temp=num 
n=temp
s=0
count=0
while(temp!=0):
    temp=temp//10
    count+=1
    
while(num!=0):
    rem=num%10  #3 5 1
    p=rem**count  #27 #125 #1 
    s=s+p    #27+125+1
    num=num//10  #0

    
if(n==s):
    print("Its a Armstrong number !")
else:
    print("Its not a Armstrong number ")    

