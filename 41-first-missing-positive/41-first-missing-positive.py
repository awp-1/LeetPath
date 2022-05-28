class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        for i in range(len(n)):
            if n[i] < 0:
                n[i] = 0
        
        for i in range(len(n)):
            val = abs(n[i])
            if 1 <= val <= len(n):
                if n[val-1] > 0:
                    n[val-1] *= -1
                elif n[val-1] == 0:
                    n[val-1] = -1*(len(n)+1)
            
        for i in range(1,len(n)+1):
            if n[i-1] >= 0:
                return i
        return len(n)+1