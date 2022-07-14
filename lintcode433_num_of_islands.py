import collections
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    # grid = [[]]
    def __new__(cls, *args, **kwargs):
        print("class new obj")
        return super().__new__(cls)
    
    def __init__(self, ext_grid):
        print("init")
        self.grid = ext_grid
    
    def __repr__(self):
        return f"self.numIslands()"
        # print(self.grid)

    def numIslands(self):
        # write your code here
        grid = self.grid
        if not grid or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        islands = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    islands += 1
                    self.markLandBFS(grid, i, j, visited)
        return islands

    def markLandBFS(self, grid, x, y, visited):
        # 1st node into queue
        queue = collections.deque([(x,y)])
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            cx, cy = queue.popleft()
            for dx,dy in DIRECTIONS:
                nx = cx + dx
                ny = cy + dy
                #print(nx, ny)
                if  0<= nx <len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] and (nx,ny) not in visited:
                    queue.append((nx,ny))
                visited.add((nx,ny))



def main():
    grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
    ob = Solution(grid)
    res = ob.numIslands()
    print("Found " + str(res) + " islands in below map:")
    for i in range(len(ob.grid)):
        print(ob.grid[i])


#main()
if __name__ == "__main__":
    main()
    # grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
    # ob = Solution(grid)
    # res = ob.numIslands()
    # print("Found " + str(res) + " islands in below map:")
    # for i in range(len(ob.grid)):
    #     print(ob.grid[i])
    
