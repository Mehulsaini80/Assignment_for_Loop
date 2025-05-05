#  21.Write a program to print fibonacci series upto n terms
#  a. Fibonacci series is a series of numbers where the current number
#  is the sum of the previous two terms. For Example: 0, 1, 1, 2, 3, 5,
#  8, 13, 21, … , (n-1th + n-2th 

num=5
a=0
b=1
c=0
print("Fibonnaci series: ") 
print(a,end=" ") 
print(b,end=" ")  
for i in range(1,num):
    c=a+b
    a=b
    b=c  
    print(c,end=" ")  
    
