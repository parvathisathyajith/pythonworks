#find the duplicate nos

arr=[1,3,4,5,4,6,5,6]
arr.sort()

duplicate_numbers=[]


for i in range(0,len(arr)-1):

    j=i+1
    if arr[j]-arr[i]==0:
        if arr[i] not in duplicate_numbers:
            duplicate_numbers.append(arr[i])

print(duplicate_numbers)

