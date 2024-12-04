student_data={
    "hari":[45,40,35],
    "gops":[35,40,45],
    "paru":[45,40,35],
    "malu":[33,38,35],
    "alan":[50,50,50]
}

#index=1 hari's avg mark
#index=5 alan's avg mark
index=5
for i,element in enumerate(student_data):
    #if i+1==index:
        marks=student_data.get(element)
        avg=sum(marks)/len(marks)
        print(element,avg)