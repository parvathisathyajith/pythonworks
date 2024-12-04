from re import finditer

f=open("C:\\Users\\parus\\OneDrive\\Desktop\\pythonworks\\regexpression_fileworks\\hashtag.txt")

for line in f:
    words=line.rstrip("\n")
    pattern="#\w+"
    matcher=finditer(pattern,words)
    for obj in matcher:
        print(obj.group())