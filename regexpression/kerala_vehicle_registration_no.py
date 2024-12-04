#starting with KL
#2digit


#alphabtes minnum1 maximum 2
#4digit

from re import fullmatch

user_input=input("enter vehicle number:-")
pattern="[KL]{0-9}{2}{a-zA-Z{1,2}{0-9}{4}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")