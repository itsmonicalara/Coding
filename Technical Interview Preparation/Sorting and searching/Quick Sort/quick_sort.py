def quicksort(a_list):
    # base case
    if len(a_list) <= 1:
        return a_list
    else:
        pivot = a_list[0]
        less = [i for i in a_list[1:] if i <= pivot]
        greater = [i for i in a_list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    my_list = [2, 3, 5, 1, 4]
    print(quicksort(my_list))
