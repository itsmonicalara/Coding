# I should return nums1
# len of nums1 = m + n
# len of nums 2 = n
# last n elements should be ignored
# zero values should not be sorted
def merge_sorted_array(nums1, m, nums2, n):
    while(len(nums1) > m or len(nums2) > n):
        del nums1[m:]
        del nums2[n:]
        break
    
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    return nums1


if __name__ == "__main__":
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6] 
    # n = 3
    nums1 = [0]
    m = 0
    nums2 = [1] 
    n = 1
    merge_sorted_array(nums1, m, nums2, n)