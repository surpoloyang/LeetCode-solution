class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xz, yz, xy = 0, 0, 0
        yzmaxlist = {}
        for i in range(len(grid)):
            xz += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    xy += 1
                yzmaxlist[j] = grid[i][j] if j not in yzmaxlist else max(yzmaxlist[j], grid[i][j])
        yz = sum(yzmaxlist.values())
        a = yz+xz+xy
        return a
Solution().projectionArea([[1,0],[0,2]])
