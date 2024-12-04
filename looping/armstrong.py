num=int(input("enter num:"))

orginal=num

digit_count=len(str(num))

total=0

while(num!=0):
    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10


print("armstrong number" if total==orginal else "not armstrong number")
