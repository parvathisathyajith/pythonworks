#spamble input

arr=[100,800,300,600,500,600,700,200]
#     0   1   2   3   4   5   6   7
 
odd_position_number=[num for index,num in enumerate(arr) if index%2!=0]
odd_position_number.reverse()
print(odd_position_number)#800,600,400,200
for index,num in enumerate(odd_position_number):
    arr[index+1]=num
print(arr)