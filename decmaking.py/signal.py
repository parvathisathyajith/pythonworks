#SyntaxError
#if condition1:
    #stmt1
#elif condition2:
    #stmt2
#elif condition3:
    #stmt3
#else:
# default stmt


signal=input("enter signal:").lower()#Will convert all letters to small letters

if signal=="red":
    print("STOP")
elif signal=="green":
    print("GO..")
elif signal=="yellow": 
    print("WAIT")
else:
    print("invalid signal")    