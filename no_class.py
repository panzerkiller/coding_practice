import collections
def numIslands(grid):
        # write your code here
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
                    markLandBFS(grid, i, j, visited)
        return islands

def markLandBFS(grid, x, y, visited):
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
    print("main(): " + str(numIslands(grid)))

if __name__ == "__main__":
    grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
    print(numIslands(grid))
    main()