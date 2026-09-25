from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visited = set()
        q  = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j, 0))

        
    
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            ny, nx, val = q.popleft()
            
            
            for dy, dx in moves:
                if 0 <= dy+ny <m and 0 <= dx+nx<n and grid[dy+ny][dx+nx] != -1:
                    if grid[dy+ny][dx+nx] >= val + 1:
                        grid[dy+ny][dx+nx] = val + 1
                        q.append((dy+ny, dx+nx, val + 1))


            











