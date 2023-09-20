"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""
a=int(input())
for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    for k in range(2*(a-i)):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    for k in range(2*(a-i)):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()
