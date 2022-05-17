def pair_socks(a_list):
    num_par = []
    socks_dict = {}

    a_list.sort()

    for ele in a_list:
        if ele in socks_dict:
            socks_dict[ele] += 1
        else:
            socks_dict[ele] = 1

    print(socks_dict)

    for ele in socks_dict:
        if(socks_dict[ele] % 2 == 0):
            num_par.append(ele)

    print(num_par)



if __name__ == "__main__":
    num_socks = [2,2,1,1]
    pair_socks(num_socks)