# 19.Write a program to check whether a number is Strong number or not
# a. Strong number is a special number whose sum of factorial digits is
# equal to the original number.
# For example: 145 is a strong number. Since, 1! + 4! + 5! = 145

num=int(input("Enter number: ")) 
temp=num 
fact=1 
sum=0

while(temp!=0):  
    rem=temp%10  
    fact=1
    for i in range(1,rem+1):    
            fact=fact*i  
            
    sum=sum+fact 
    temp=temp//10  
 
print("sum=",sum)
print("num=",num)  

if(sum==num): 
    print("It's Strong number")   
else:
    print("Not a Strong number")  

