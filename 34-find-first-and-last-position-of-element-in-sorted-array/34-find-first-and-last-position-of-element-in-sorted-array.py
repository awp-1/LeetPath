class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        
        ans = [-1,-1]
        if len(nums) == 1 and nums[l] == target:
            ans[0] = 0
            ans[1] = 0
            return ans
            
        
        while l<=r:
            if nums[r] == target and ans[1] == -1:
                ans[1] = r
                while r > 0 and nums[r-1] == target:
                    r -= 1
                ans [0] = r
            r -= 1
            if nums[l] == target and ans[0] == -1:
                ans[0] = l
                while l<len(nums)-1 and nums[l+1] == target:
                    l +=1
                ans[1] =l
            print(l)
            l +=1
        return ans
        
        