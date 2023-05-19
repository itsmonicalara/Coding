# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
def sockMerchant(n, arr):
    count = 0
    arr.sort()
    ele = 1
    while ele < n:
        if arr[ele] == arr[ele - 1]:
            count += 1
            ele += 2
        else:
            ele += 1
    return count

if __name__ == '__main__':
    n = 9
    arr = [10,20, 20, 10, 10, 30, 50, 10, 20]
    sockMerchant(n, arr)
