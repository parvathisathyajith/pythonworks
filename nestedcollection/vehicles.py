cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]



#print count of vechiles

print(f"total vechiles=>{len(cars)}")

#print available colors of baleno

baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]

print(baleno_colors[0])

#print all brands

all_brands=[c.get("brand") for c in cars]
print(set(all_brands))

#print car names availablen in amt transmission

cars_amt=[ c.get("name")for c in cars if "amt" in c.get("transmissions")]
print(cars_amt)

#colors available in blue cars

car_colors=[ c.get ("name") for c in cars if "blue" in c.get("colors")]
print(car_colors)

#all transmission

all_transmission={t for c in cars for t in c.get("transmissions")}
print(all_transmission)

#print all colors

all_colors={color for c in cars for color in c.get("colors")}
print(all_colors)

#most popular color
#{"blue":4, "red":2}

popular_clr=[("colors")for c in cars]


#print(clr_count)

#mostly cars

costly_cars=max(cars,key=lambda d:d.get("price"))

print(costly_cars.get("name"))

low_cost=min(cars,key=lambda d:d.get("price"))

print(low_cost.get("name"))

#sorted cars

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_cars_name={c.get("name"):[c.get("price"),c.get("brand")]for c in sorted_cars}

print(sorted_cars_name)