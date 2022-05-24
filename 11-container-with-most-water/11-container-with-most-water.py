class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l,r = 0, len(height)-1
        
        while l<r:
            water = (r-l)*min(height[l],height[r])
            ans = max(ans,water)
            if height[r] < height[l]:
                r -=1
            else:
                l +=1
           
        print(ans)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         hei = min(height[i],height[j])
        #         ans = max(ans,(j-i)*hei)
        # return ans