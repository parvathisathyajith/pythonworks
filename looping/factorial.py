#print factorial of number

number=int(input("enter a number:"))

factorial=1

for number in range(1,number+1):

    factorial=factorial*number
print(factorial)    