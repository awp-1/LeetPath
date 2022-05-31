class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        
        while q:
            size = len(q)
            
            while size>0:
                size -=1
                i = q.popleft()
                
                if i - arr[i] >= 0:
                    if arr[i - arr[i]] == 0:
                        return True
                    elif arr[i - arr[i]] > 0:
                        q.append(i - arr[i])
                
                if i + arr[i] <= len(arr)-1:
                    if arr[i + arr[i]] == 0:
                        return True
                    elif arr[i + arr[i]] > 0:
                        q.append(i + arr[i])
                
                arr[i] = -1
                
        return False