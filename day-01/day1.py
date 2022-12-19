int1=int(input())
int2=int(input())

for i in range(int1,int2+1):
    if i%3==0:
        print('Foo')
    elif i%2==0:
        print('Bar')
    else:
        print('Baz')