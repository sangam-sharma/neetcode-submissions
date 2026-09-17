class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS=len(grid),len(grid[0])
        maximum=0
        
        def bfs(r,c)->int:
            q=deque()
            grid[r][c]=0
            
            q.append((r,c))
            count=1
            while q:
                rows,cols=q.popleft()
                for dr,dc in directions:
                    nr,nc=rows+dr,cols+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]==0:
                        continue

                    
                    q.append((nr,nc))
                    grid[nr][nc]=0
                    count+=1
            return count



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    maximum=max(maximum,bfs(r,c))

        return maximum

