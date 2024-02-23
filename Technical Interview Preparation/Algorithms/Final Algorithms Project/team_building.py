def team_building(my_list):
    temp_list = []
    first_team = []
    second_team = []
    for lst in my_list:
        for elem in lst:
            if elem == 0:
                index = lst.index(0)
                print("Not Worked")
            else:
                if(lst.count(lst[0]) == len(lst)):
                    print(-1)
                    return -1
        new_value = [my_list.index(lst) + 1, index + 1]
        temp_list.append(new_value)
    for team in temp_list:
        # TODO: Half of the temp_list instead of the first team
        if len(first_team) < 2:
            if team not in first_team and list(reversed(team)) not in first_team:
                first_team.append(team)
        else:
            if team not in second_team and list(reversed(team)) not in second_team:
                second_team.append(team)

    for x in first_team:
        print(" ".join(map(str, x)))
    for y in second_team:
        print(" ". join(map(str, y)))


if __name__ == '__main__':
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(map(int, input().rstrip().split())))
    team_building(lst)
