def twoSum(nums, target):
    l = len(nums)
    a = []
    for i in range(l-1):
        for j in range(i+1,l):
            if nums[i]+nums[j] == target:
                return [i, j]
    return [0, 0]