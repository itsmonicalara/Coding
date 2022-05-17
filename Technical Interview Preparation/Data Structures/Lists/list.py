def print_list(list):
    for ele in list:
        print(ele)

def reversed_list(list):
    reversed = list[::-1]
    return reversed
        

if __name__ == '__main__':
    my_list = ['car', 1, 2, 'bus']
    print_list(my_list)
    reversed = reversed_list(my_list)
    print_list(reversed)