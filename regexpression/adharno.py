from re import fullmatch

adhar_no=input("enter adhar_no:-")
pattern="[0-9]{4}[0-9]{4}[0-9]{4}"

matcher=fullmatch(pattern,adhar_no)

if matcher==None:
    print("invalid")

else:
    print("valid")