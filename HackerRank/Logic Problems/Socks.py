def socks(n, ar):
    count = 0
    for i in range(0, n-1):
        if(i < n and ar[i] == ar[i+1]):
            count = +1
            i = +1
    print(count)


n = int(input())
ar = list(map(int, input().rstrip().split()))
socks(n, ar)
