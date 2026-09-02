class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        i = 0

        while i < len(nums):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
            i += 1
