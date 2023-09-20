"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

a=int(input())
b=1
for i in range(2,a+2):
    for  k in range(a-i+1):
        print(" ",end="")
    for j in range(1,i):
        print(chr(64+j),end="")
    for l in range(i-1,1,-1):
        print(chr(64+l-1),end="")
    print()
