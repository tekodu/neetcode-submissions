class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        current_prefix = 1
        for i in range(n):
            prefix[i] = current_prefix
            current_prefix *= nums[i]

        suffix = [1] * n
        current_suffix = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = current_suffix
            current_suffix *= nums[i]

        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res