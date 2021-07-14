def team_building(my_list):
    temp_list = []
    first_team = []
    second_team = []
    for lst in my_list:
        for elem in lst:
            if elem == 0:
                index = lst.index(0)
                print("Not Worked")
        new_value = [my_list.index(lst) + 1, index + 1]
        temp_list.append(new_value)
    for team in temp_list:
        if team not in first_team and list(reversed(team)) not in first_team:
            first_team.append(team)
    for x in first_team:
        print(" ".join(map(str, x)))

# TODO: Add case if all are 1
# TODO: It needs to take in account all zeros

'''
def team_building(my_list):
    team_1 = []
    team_2 = []
    my_list = sorted(my_list)
    for lst in my_list:
        for elem in lst:
            if elem == 0:
                team_1.append(elem + 1)
            else:
                team_2.append(elem + 1)
    if len(team_1) > len(team_2):
        print(-1)
    else:
        print(team_1, team_2)
'''


if __name__ == '__main__':
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(map(int, input().rstrip().split())))
    team_building(lst)
