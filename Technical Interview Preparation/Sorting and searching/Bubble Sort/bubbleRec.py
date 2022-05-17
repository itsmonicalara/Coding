# Running Time: 0.087s
def bubble(num, unordered_list):
    # base case
    if num == 1:
        return unordered_list
    # The recursion replaces the outer loop
    for i in range(num - 1):
        if(unordered_list[i] > unordered_list[i + 1]):
            # swap the elements
            unordered_list[i], unordered_list[i + 1] = unordered_list[i + 1], unordered_list[i]
    print(bubble(num - 1, unordered_list))

if __name__ == '__main__':
    number = 5
    a_list = [4, 3, 1, 2, 5]
    print(a_list)
    bubble(number, a_list)