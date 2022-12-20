nooftri=int(input())
tris = [list(map(int,input().split())) for i in range(nooftri)]
print(tris)
for i,tris in enumerate(tris):
        tris.sort()
        if i % 3 == 0:
            print(tris[0])
        elif i % 3 == 1:
            print(tris[1])
        else:
            print(tris[2])
