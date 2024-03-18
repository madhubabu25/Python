size=6
for i in range(size):
    for j in range(1,size):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(65+k),end="")
    print()    