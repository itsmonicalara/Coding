def minimumBribes(q):

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)

# Number of people who overtake a person, theres no need to do sorting // No more than 2 bribes
