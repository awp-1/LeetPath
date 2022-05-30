class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row ,col = len(grid),len(grid[0])
        visited = set()
        island = 0
        
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                r,c = q.popleft()
                direction=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direction:
                    if (r+dr in range(row) and c+dc in range(col)
                    and grid[r+dr][c+dc] =='1' and (r+dr,c+dc) not in visited):
                        visited.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
            
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    island +=1
        return island 
        