arr=[1,3,4,5]
# num=1
# for i in range(0,len(arr1)):
#     if num==arr1[i]:
    
#         num=num+1
#     else:
#             break
# print(num)
arr.sort()



for i in range(0,len(arr)-1):
    j=i+1
    
    if arr[j]-arr[i]!=1:

        print(arr[i]+1,"is missing")
        break