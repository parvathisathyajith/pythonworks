num1=int(input("enter the 1st no:"))
num2=int(input("enter the 2nd no:"))
num3=int(input("enter th 3rd no:"))

if num1>num2 and num2>num3:
    if num2>num3:
      print(f"{num2} is second largest")
    else: 
      print(f"{num3} is second largest")

elif num2>num1 and num2>num3:
    if num1>num3:
      print(f"{num1} is  second larger")
    else:
      print(f"{num3} is second larger") 

elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"{num1} is the second largest") 
    else:
        print(f"{num2}is the second largest")
else:
    print(f"{num1}={num2}={num3}")                