def greatest_common(str1, str2):
    times = 0
    if str2 in str1:
        times = str1.count(str2)
        if times >= 1:
            return str2
    else:
        return ''

if __name__ == "__main__":
    str1 = 'ABCABC'
    str2 = 'ABC'
    print(greatest_common(str1, str2))
