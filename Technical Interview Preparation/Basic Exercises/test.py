# Function to count the number of pairs in a list of numbers
def find_pairs(a_list):
    num_pairs = 0
    a_list.sort()

    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            if a_list[i] == a_list[j]:
                num_pairs += 1
                break

    return num_pairs


if __name__ == "__main__":
    num_socks = [2,2,1,1,2]
    print(find_pairs(num_socks))