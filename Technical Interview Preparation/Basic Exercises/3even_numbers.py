def even_numbers(a_list):
    even_list = []
    for ele in a_list: 
        if(ele % 2 == 0):
            even_list.append(ele)

    print(even_list)


if __name__ == "__main__":
    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    even_numbers(numbers)