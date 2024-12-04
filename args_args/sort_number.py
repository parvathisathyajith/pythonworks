op=input("enter the operation")
def sort_numbers(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)
    if kwargs.get("reverse")=="False":
        return sorted(args,reverse=False)

print(sort_numbers(1,2,3,4,reverse=op))