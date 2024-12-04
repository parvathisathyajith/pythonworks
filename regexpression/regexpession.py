from re import finditer

text="fatcatrunsveryfasttocaththerat"

matcher=finditer("at",text)# [(start,group),(),()]

for obj in matcher:
    print(obj.start(),obj.group())

    print(obj.start(),obj.group())
