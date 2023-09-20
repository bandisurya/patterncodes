"""
1
22
333
4444
55555
"""

x=int(input())
for i in range(x+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
