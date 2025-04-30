# Program to find the LCM of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

n=num1
i=2
print("LCM of",num1,"=",end=" ")
while(i<=n):
        if(n%i==0):
                print(i,end=" ")
                n=n//i;
        else:
                i+=1
                
print()

print("LCM of",num2,"=",end=" ")
n2=num2
i=2
while(i<=n2):
        if(n2%i==0):
                print(i,end=" ") 
                n2=n2//i 
        else:
                i+=1
                
