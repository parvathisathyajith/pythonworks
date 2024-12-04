#  c1 c2 c3
#  *  *  *
#  *  *  *
#  *  *  *
#  *  *  *
#  *  *  *
#

for row in range(1,7):

    for col in range(1,4):

       print("*",end="\t")

    print()    


# $  

# $  $ 

#$    $    $
# $     $     $    $
# $    $    $     $    $
# $    $     $    $    $    $   

for row in range(1,7):
    for col in range(1,7):
        print("$",end="\t")
    print()  

# 1
# 2  2
# 3  3    3  
# 4   4   4     4
# 5   5   5    5     5  

for row in range(1,6):

    for col in range(1,row+1):

       print(row,end="\t")
    print() 

# *   *    *    *   *
# *   *    *    *
# *   *    *
# *   *
# *

for row in range(5,0,-1):
    for col in range(1,row+1):
        print("*",end="\t")
    print()    

# col 

    for row in range(1,6):
        for col in range(5,row-1,-1):  
            print("*",end="\t")
        print()      