n,m = tuple(map(int, input().split()))

c=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if i%2==0:
            print(i*m-j+1, end=' ')
        else:
            print(c,end=' ')
        c+=1
    print()