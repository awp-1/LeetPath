class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time,first = 0,0
        row , col = len(grid),len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    first += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        print(q)           
        distance = [[0,-1],[0,1],[-1,0],[1,0]]
        
        while q and first > 0:
            
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in distance:
                    row , col = dr+r, dc+c
                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    q.append([row,col])
                    first -= 1
                    print(grid)
            print(time,q,first)
            time += 1
            print(time,q,first)
        return time if first == 0 else -1
                    