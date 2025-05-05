# 17.Write a program to find all prime factors of a number.

num=18


for i in range(2,num+1):
    
    if(num%i==0):        
        j=2
        count=0
        while(j<i):
            if(i%j==0): 
                
                count=1  
                break
            j+=1 
                
        if(count==0): 
            print(i)         
                
