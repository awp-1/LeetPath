class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row ,col = len(grid),len(grid[0])
        visited = set()
        island = 0
        
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                r,c = q.popleft()
                direction=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direction:
                    if (r+dr in range(row) and c+dc in range(col)
                    and grid[r+dr][c+dc] ==1 and (r+dr,c+dc) not in visited):
                        visited.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
                        area +=1
            return area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island =max(island,bfs(r,c))                    
                    
        return island 