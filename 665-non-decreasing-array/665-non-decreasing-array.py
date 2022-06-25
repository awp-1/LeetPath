class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        i = 1
        while i < len(nums):
            if nums[i-1] > nums[i]:
                if flag or (i>1 and i<len(nums)-1 and nums[i-2] > nums[i] and nums[i-1] > nums[i+1]):
                    return False
                
                flag = 1 
            i += 1
        return True