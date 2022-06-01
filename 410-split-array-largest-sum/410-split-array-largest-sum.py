class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l,r = max(nums),sum(nums)
        res = r 
        
        def canSplit(largest):
            curSum = 0
            subarry = 0
            for n in nums:
                curSum += n
                if largest < curSum:
                    subarry +=1
                    curSum = n
            return subarry+1 <= m
        
        while l<=r:
            mid = l+((r-l)//2)
            
            if canSplit(mid):
                res = mid
                r = mid -1
            else: 
                l = mid+1
        return res
    