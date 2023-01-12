from collections import Counter

def find_facebook(string):
    string_counter = Counter(string)

    for char in 'facebook':
        string_counter[char] -= 1
        if string_counter[char] < 0:
            return 'NO'

    return 'YES'

def main():
    t = int(input())
    for i in range(t):
        word = input()
        print("Case #{}: {}".format(i+1, find_facebook(word)))

main()
