class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        minheap=[[grid[0][0],0,0]]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while minheap:
            t,r,c=heapq.heappop(minheap)
            if r==n-1 and c==n-1:
                return t
            
            for nr,nc in directions:
                rows,cols=r+nr,c+nc
                if rows<0 or cols<0 or (rows,cols) in visit or rows==n or cols==n:
                    continue
                visit.add((rows,cols))
                heapq.heappush(minheap,[max(t,grid[rows][cols]),rows,cols])
