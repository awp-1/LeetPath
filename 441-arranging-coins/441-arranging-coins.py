class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1,n+1):
            n = n - i
            if n == 0:
                return i
            elif n < 0 :
                return i-1