t=int(input())
while t:
    t-=1
    r,c=map(int,input().split())
    if r!=c:
        a=min(r,c)+(int((abs(r-c)-1)/2)+1)
        print(20)
        print(a,end=' ')
        print(a)
    else:
        print(19)
    print('1 1')
    print('8 8')
    print('7 7')
    print('8 6')
    print('3 1')
    print('4 2')
    print('5 1')
    print('8 4')
    print('7 3')
    print('8 2')
    print('7 1')
    print('1 7')
    print('2 8')
    print('4 6')
    print('6 8')
    print('1 3')
    print('2 4')
    print('1 5')
    print('4 8')