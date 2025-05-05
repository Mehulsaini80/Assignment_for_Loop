#  20.Write a program to check whether a number is perfect number or not
# a. Perfect number is a positive integer which is equal to the sum of
#  its proper positive divisors.
#  For example: 6 is the first perfect number
#  Proper divisors of 6 are 1, 2, 3
#  Sumofits proper divisors = 1 + 2 + 3 = 6.
#  Hence 6 is a perfect number

n=28
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i 
if(sum==n):
    print("It's a perfect number ")
else:
    print("It's not a perfect number")  