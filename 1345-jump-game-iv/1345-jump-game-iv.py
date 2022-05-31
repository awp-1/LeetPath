class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        hasmap = defaultdict(list)        
        for index in range(len(arr)):
            hasmap[arr[index]].append(index)
        print(hasmap) 
        q = deque()
        q.append(0)
        if n == 1:
            return 0
        
        step = 0
        
        while q:
            size = len(q)
            step += 1
            while size>0:
                size -=1
                i = q.popleft()
                
                if i -1 > 0 and arr[i-1] in hasmap: 
                    q.append(i-1)
                    
                if i + 1 <n and arr[i+1] in hasmap:
                    if i+1 == n-1:
                        return step
                    q.append(i+1)
                    
                if arr[i] in hasmap:                    
                    for j in hasmap[arr[i]]:
                        if j != i:
                            if j == n-1:
                                return step
                            q.append(j)
                if arr[i] in hasmap:
                    hasmap.pop(arr[i])
        return step                   