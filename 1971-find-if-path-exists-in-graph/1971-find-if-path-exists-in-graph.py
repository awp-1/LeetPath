class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_matric = defaultdict(list)
        
        for node1,node2 in edges:
            adj_matric[node1].append(node2)
            adj_matric[node2].append(node1)
            
        visited = set()
        def dfs(node):
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                for i in adj_matric[node]:
                    result = dfs(i)

                    if result:
                        return True
            
        return dfs(start)
                