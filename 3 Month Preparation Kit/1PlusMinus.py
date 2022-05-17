def plus_minus(a_list, n):
    pos_num, neg_num, zero_num = 0, 0 ,0
    for ele in a_list:
        # proportion of positive values
        if ele > 0:
            pos_num += 1
        # proportion of negative values
        elif ele < 0:
            neg_num += 1
        # proportion of zeros
        else:
            zero_num += 1

    pos_list = pos_num / n  
    neg_list = neg_num / n
    zero_list = zero_num / n

    print('{0:.6f}'.format(pos_list),
        '{0:.6f}'.format(neg_list),
        '{0:.6f}'.format(zero_list),
        sep='\n')    


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(arr)
    plus_minus(arr, n)

