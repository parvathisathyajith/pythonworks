def second_max_number(*args):
    sorted_numbers=sorted(args,reverse=True)
    return sorted_numbers[1]


print(second_max_number(10,11,12,13))
print(second_max_number(10,11,12,13,14,15))


def display_mobile_data(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("price"))
display_mobile_data(name="oneplus",price=3200,display="amoled")   
