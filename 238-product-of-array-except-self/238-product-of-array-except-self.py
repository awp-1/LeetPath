class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # ans = []
        # for i in range(len(nums)):
        #     val =1 
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         val = val*nums[j]
        #     ans.append(val)
        # return ans
        
        
        
        
        pref = 1
        post = 1
        
        ans =[]
        ans.append(pref)
        
        for i in range(len(nums)-1):
            ans.append(ans[i]*nums[i])
        print(ans)
        for i in range(len(nums)-1,0,-1):
            post = post*nums[i]
            ans[i-1] = ans[i-1]*post
            print(ans[i-1])
        print(ans)
        return ans