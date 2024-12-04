#calculator(10,20,30,oprations="+")
#calculator(10,11,12,13,14,operation="*")

def calculator(*args,**kwargs):
    if kwargs.get("operation")=="+":
       return sum(args)
    if kwargs.get("operation")=="*":
        result=1
        for num in args:
             result=result*num
        return result
print(calculator(10,20,30,operation="*"))            


