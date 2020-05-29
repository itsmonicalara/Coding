def counting_valleys(n,s):
    valleys = 0
    level = 0
    for i in range(0,n):
        if(s[i] == "U"):
            level += 1
        if(s[i] == "D"):
            level -= 1
        if(level == 0 and s[i] == "U"):
            valleys += 1
    print(valleys)

n = int(input())
s = input()
counting_valleys(n,s)
   
