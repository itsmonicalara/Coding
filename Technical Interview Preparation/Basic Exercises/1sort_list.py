def sort_list(a_list):
    sorted_list = []
    # Asumimos arbitrariamente que el primer numero de la lista es el mayor numero
    while a_list:
        max_num = a_list[0]
        for ele in a_list:
            if ele < max_num:
                max_num = ele
        sorted_list.append(max_num)
        a_list.remove(max_num)

    print(sorted_list)

        
if __name__ == "__main__":
    unsorted_list = [3,4,2,1,6,3,5]
    sort_list(unsorted_list)