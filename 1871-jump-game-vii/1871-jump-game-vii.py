class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        f =0
        while q:
            i = q.popleft()
            start = max(i+minJump , f+1)
            for j in range(start,min(i+maxJump,len(s)-1)+1):
                if s[j] == '0':                                       
                    q.append(j)
                    if j == len(s)-1:
                        return True
            f = i + maxJump
        return False
    
            