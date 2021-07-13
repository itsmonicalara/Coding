def team_building(my_list, n):
    temp_list = []
    for lst in my_list:
        for elem in lst:
            if elem == 0:
                index = lst.index(0)
                print("Not Worked")
            elif elem == 1:
                print("Worked")
            # TODO: Add case if all are 1
            # TODO: It needs to take in account all zeros

        new_value = [my_list.index(lst) + 1, index + 1]
        temp_list.append(new_value)
    print(temp_list)


if __name__ == '__main__':
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(map(int, input().rstrip().split())))
    team_building(lst, n)
