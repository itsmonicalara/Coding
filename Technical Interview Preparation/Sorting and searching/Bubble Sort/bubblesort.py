def bubble(num, unordered_list):
    # to get the biggest ele at the end of the list
    for i in range(num):
        # to sort all the elements
        for j in range(num - 1):
            if(unordered_list[j] > unordered_list[j + 1]):
                # swap the elements
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]

    print('Sorted list:',unordered_list)

if __name__ == '__main__':
    number = 5
    a_list = [4, 3, 1, 2, 5]
    print('Unsorted list:', a_list)
    bubble(number, a_list)