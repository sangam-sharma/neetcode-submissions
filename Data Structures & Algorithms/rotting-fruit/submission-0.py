class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        
        minutes=0
        fresh=0
        q=collections.deque()

        


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                   q.append([r,c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh>0 and q:
            length= len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr,dc in directions:
                    rows,cols=dr+r,dc+c
                    if rows in range(ROWS) and cols in range(COLS) and grid[rows][cols]==1:
                        grid[rows][cols]=2
                        q.append((rows,cols))
                        fresh-=1
            minutes+=1



        
        return minutes if fresh == 0 else -1
                    

        