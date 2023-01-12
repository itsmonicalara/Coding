def plus_minus(a_list, n):
    pos_num, neg_num, zero_num = 0, 0 ,0
    for ele in a_list:
        if ele > 0:
            pos_num += 1
        elif ele < 0:
            neg_num += 1
        else:
            zero_num += 1

    print('{0:.6f}'.format(pos_num / n),
        '{0:.6f}'.format(neg_num / n),
        '{0:.6f}'.format(zero_num / n),
        sep='\n')    


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plus_minus(arr, n)

