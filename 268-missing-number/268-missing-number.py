class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)
        for i in range(len(nums)):
            if nums[i] - i != 0:
                a = i
                break
        return a