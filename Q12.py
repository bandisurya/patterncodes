"""
1        1
12      21
123    321
1234  4321
1234554321
"""

x=int(input())
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(2*x-2*i):
        print(" ",end="")
    for l in range(i,0,-1):
        print(l,end="")
    print()
