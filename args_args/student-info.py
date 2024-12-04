#def student_info(45,43,44,operation="avg")
#def student_info(45,43,44,operation="total")

def student_info(*args,**kwargs):
    if kwargs.get("operation")=="avg":
        return sum(args)/len(args)
    if kwargs.get("operation")=="total":
        return sum(args)
print(student_info(45,43,44,operation="avg"))       


