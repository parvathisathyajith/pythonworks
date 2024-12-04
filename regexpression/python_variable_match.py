from re import fullmatch

user_input=input("enter the variable name")#num_

#start with an alphabet(lowercase,uppercase)
#any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)#none

if matcher==None:
    print("invalid")
else: 
    print("valid")   
