num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1>num2 and num1>num3:
    print(f"{num1}is larger")
elif num2>num1 and num2>num3:
    print(f"{num2}is larger")
elif num3<num1 and num3>num2: 
    print(f"{num3}is larger")      
else:
    print(f"{num1}={num2}={num3}")
