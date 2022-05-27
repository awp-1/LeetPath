class Solution:
    def numberOfSteps(self, n: int) -> int:
        i = 0
        while n:
            if n%2 == 0:
                n = n//2
            else:
                n = n-1
            i += 1
            
        return i