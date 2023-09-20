"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""

x=int(input())
for i in range(1,x+1):
    for k in range(1,x+1-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(x+1,0,-1):
    for k in range(x-i+1,0,-1):
        print(" ",end="")
    for j in range(2*i-2,1,-1):
        print("*",end="")
    print()
