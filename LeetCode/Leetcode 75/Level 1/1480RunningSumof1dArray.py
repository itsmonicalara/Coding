# TODO:
# Give me the time complexity of this code

def running_sum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] += numbers[i - 1]
    print(*numbers)

if __name__ == "__main__":
    nums = [1,2,3,4]
    running_sum(nums)
