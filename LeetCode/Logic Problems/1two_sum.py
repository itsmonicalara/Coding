
def twoSum(nums, target) :
    # Iterate through the num list
    for i in range(len(nums)):
        # Iterate each element in the num list
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]

nums_list = [2,7,11,15]
target = 9
twoSum(nums_list, target)