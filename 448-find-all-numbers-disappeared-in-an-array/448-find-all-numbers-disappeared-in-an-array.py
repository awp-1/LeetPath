class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        lent = len(nums)
        nums = set(nums)
        ans = []
        print(nums)
        for i in range(1,lent+1):
            if i not in nums:
                ans.append(i)
        return ans