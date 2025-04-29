#12.Write a program to find all factors of a number.

num=int(input("Enter a number: "));

for i in range(1,num):
    if(num%i==0):
        print(i);
        