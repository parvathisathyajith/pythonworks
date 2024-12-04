#num is perfect=28,6

#1,num

num=int(input("enter no"))

total=0

for i in range(1,num):

    if num%i==0:

        total=total+i
print("perfect"if total==num else "not perfect")
        
