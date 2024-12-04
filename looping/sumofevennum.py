total=0
for num in range(1,11,1):
    if num%2==0:
        digit=num%10
        total=total+digit
    print(total)