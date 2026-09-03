class Solution(object):

    def productExceptSelf(self, nums):

        result = [1] * len(nums)

        product = 1

        # Left product
        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        product = 1

        # Right product
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result