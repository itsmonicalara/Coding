def change(d,n,m):
    if m == 0:
        return 0
    elif n < 0:
        return 10008000
    else:
        return min(change(d,n-1,m),change(d,n-1,m%d[n]) + m//d[n])

d = [1,2,8,10]
n = len(d)
m = 20
print(change(d,n-1,m))