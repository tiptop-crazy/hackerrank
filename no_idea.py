if __name__=='__main__':
    n,m =map(int,raw_input().split())
    arr=map(int,raw_input().split())
    a=set(map(int,raw_input().split()))
    b=set(map(int,raw_input().split()))

    hapiness=0

    for num in arr:
        if num in a:
            hapiness+=1
        elif num in b:
            hapiness-=1
    print hapiness
