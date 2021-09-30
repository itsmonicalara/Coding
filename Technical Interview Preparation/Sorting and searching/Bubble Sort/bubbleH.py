def bubble(num, unordered_list):
    num_swaps = 0
    # to get the biggest ele at the end of the list
    for i in range(num):
        # to sort all the elements
        for j in range(num - 1):
            if(unordered_list[j] > unordered_list[j + 1]):
                num_swaps = num_swaps + 1
                # swap the elements
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]

    print('Array is sorted in',num_swaps,'swaps.')
    print('First Element:',unordered_list[0])
    print('Last Element:',unordered_list[-1])
if __name__ == '__main__':
    number = int(input().strip())
    a_list = list(map(int, input().rstrip().split()))
    bubble(number, a_list)