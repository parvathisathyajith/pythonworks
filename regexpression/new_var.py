#starting with an alphabet from p-t
#in second place must be a number that is \ by 3
#followed by anynumber alphabet,numbers,@

#s6abc
#a6vvhvh
#s7bc
from re import fullmatch

user_input=input("enter a variable name:-")

pattern="[a-zA-Z][a-zA-Z0-9]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")