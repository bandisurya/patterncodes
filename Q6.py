"""
1
12
123
1234
12345
"""
x=int(input())
for i in range(x+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
