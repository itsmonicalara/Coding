def duplicate(a_list):
    unique_list = []
    for ele in a_list:
        if ele not in unique_list:
            unique_list.append(ele)
    
    print(unique_list)


if __name__ == "__main__":
    numbers = [1,2,2,3,4,4,5,5,6]
    duplicate(numbers)