class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        st=[]
        area=0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]==1 and (r,c) not in visit:
                    st.append([r,c])
                    visit.add((r,c))
                    curr=0
                    while st:
                    
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        rows,cols=st.pop()
                        curr+=1

                        for dr,dc in directions:
                            nr,nc=rows+dr,cols+dc
                            if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visit or grid[nr][nc]==0:
                                continue
                        
                            visit.add((nr,nc))
                            st.append([nr,nc])
                    area=max(area,curr)
        return area


        
