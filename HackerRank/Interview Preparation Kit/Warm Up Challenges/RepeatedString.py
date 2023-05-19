# There is a string, s , of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n , find and print the number of letter a's in the first  letters of the infinite string.

def repeated_string(s, n):
    pattern_count = s.count('a')  # Count occurrences of 'a' in the pattern 
    full_repeats = n // len(s)  # Calculate the number of full pattern repeats   
    remaining = n % len(s)  # Calculate the length of the remaining substring   
    remaining_count = s[:remaining].count('a') if remaining > 0 else 0  # Count occurrences in the remaining substring
    result = pattern_count * full_repeats + remaining_count  # Calculate the total count
    
    return result


if __name__ == '__main__':
    # s = 'abcac'
    # n = 10
    s = 'a'
    n= 1000000000000
    print(repeated_string(s, n))