# # 16.Write a program to print all Prime numbers between 1 to n.
num = int(input("Enter a number: "))
j = 2

while j <= num:
    i = 2 
    
    count = 0
    
    while i < j:  #2<3 3<4
        
        if j % i == 0: 
            
            count = 1
            
            break
        i += 1
        
    if count==0:
        print(j) 
    j += 1
