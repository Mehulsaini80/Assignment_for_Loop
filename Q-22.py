#  22.Write a program to find ones complement of a binary number
#  a. One's complement of a binary number is defined as value
#  obtained by inverting all binary bits. It is the result of swapping all
#  1s to 0s and all 0s to 1s


n=input("Enter a number: ")
ch=''
com=""
    
for ch in n:
    if(ch=='0'): 
        com=com+'1' 
    else:
        com=com+'0'
        
print("One's compliment is: ",com)  


