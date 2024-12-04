num=int(input("enter the num:"))

if num%15==0:
    print("fizzbuzz")
elif num%5==0:
    print("buzz")
elif num%3==0:
    print("fizz")
else:
    print("invalid number")
