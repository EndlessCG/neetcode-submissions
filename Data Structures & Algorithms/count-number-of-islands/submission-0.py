class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        cnt = 0
        queue = []
        for gl_i in range(len(grid)):
            for gl_j in range(len(grid[0])):
                if grid[gl_i][gl_j] == "1" and (gl_i, gl_j) not in seen:
                    queue = [(gl_i, gl_j)]
                    cnt += 1
                while queue: 
                    i, j = queue[0]
                    queue = queue[1:]
                    if (i, j) in seen:
                        continue
                    seen.add((i, j))
                    if grid[i][j] == "1":
                        if i > 0:
                            queue.append((i - 1, j))
                        if i < len(grid) - 1:
                            queue.append((i + 1, j))
                        if j > 0:
                            queue.append((i, j - 1))
                        if j < len(grid[0]) - 1:
                            queue.append((i, j + 1))
        return cnt



