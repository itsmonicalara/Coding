# given an arrat of integers numbers, build a new array from numbers using the following rules:
# include numbers[i] in the new array if it is greater than both of its nearest lef neighbours (if they exist)

def main():
    numbers = [3, 2, 1, 4, 5, 6, 0, -1, -2, -3]
    print(numbers)
    print(process_array(numbers))
 
 
def process_array(array):
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            array[i] = array[i]
        else:
            array[i] = 0
    print(array)
