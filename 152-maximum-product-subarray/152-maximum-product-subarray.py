class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max,cur_min = 1,1
        for i in nums:
            prod_max = cur_max*i
            prod_min = cur_min*i
            
            cur_max = max(prod_max,prod_min,i)
            cur_min = min(prod_max,prod_min,i)
            
            res = max(res,cur_max)
        return res