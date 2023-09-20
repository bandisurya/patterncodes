"""
   *
  ***
 *****
*******
"""
x=int(input())
for i in range(1,x+1):
    for k in range(x-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
