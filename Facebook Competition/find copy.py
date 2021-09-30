def find_facebook(some_string):
    if set("facebook").issubset(some_string):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        word = input()
        print("Case #{}: {}".format(i+1, find_facebook(word)))

main()


