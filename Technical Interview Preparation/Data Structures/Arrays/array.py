def reverse_array(array):
    reversed = array[::-1]
    return reversed

# if array contains zero move them at the beginnig of array
def move_zeros(array):
    zeros = 0
    for i in array:
        if i == 0:
            zeros += 1
    for i in range(zeros):
        array.remove(0)
    for i in range(zeros):
        array.insert(0, 0)
    return array


if __name__ == '__main__':
    an_array = [1, 2, 3, 0, 4, 0, 10]
    print(*an_array)
    new_array = move_zeros(an_array)
    print(*new_array)


    