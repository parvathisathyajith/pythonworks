from re import findall 
f=open("C:\\Users\\parus\\OneDrive\\Desktop\\pythonworks\\regexpression_fileworks\\date.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
dates=findall(pattern,content)
for d in dates:
    print(d)