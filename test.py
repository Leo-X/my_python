# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9


nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        j = i+1
        while j < len(nums):
            if nums[i]+nums[j] == target:
                return [i, j]
            j += 1


print('key:', twoSum(nums, target))

