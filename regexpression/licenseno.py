from re import fullmatch

license_no=input("enter the license_no:-")
pattern="[A-Z]{2}[0-9]{2}[0-9]{11}"

matcher=fullmatch(pattern,license_no)

if matcher==None:
    print("invalid")

else:
    print("valid")