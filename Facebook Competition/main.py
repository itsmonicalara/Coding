import random
import string

def consistency(some_string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    if isinstance(some_string, str):
        print('This variable is a string!')
        # Turn the string into uppercase
        if any(substring in some_string.upper() for substring in vowel):
            print('There are vowels')
            random_vowel = random.choice(vowel)
            for ele in vowel:
                some_string = some_string.replace(ele, random_vowel)
        else:
            print('No voewls')
    else:
        print('This variable is no a string.')


if __name__ == '__main__':
    word = 'mom'
    consistency(word)
