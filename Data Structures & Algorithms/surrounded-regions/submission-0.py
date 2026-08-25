class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = []
        visited = set()
        islands = {}
        islands_surrounded = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) in visited or board[i][j] == 'X':
                    continue
                island_cnt = len(islands)
                islands_surrounded[island_cnt] = True
                islands[island_cnt] = []
                queue.append((i, j, island_cnt))
                while queue:
                    x, y, island_cnt = queue.pop(0)
                    # print(x, y, board[ x][y], islands, islands_surrounded)
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    if board[x][y] == 'X':
                        continue
                    if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                        islands_surrounded[island_cnt] = False
                    islands[island_cnt].append((x, y))
                    if x > 0:
                        queue.append((x - 1, y, island_cnt))
                    if x < len(board) - 1:
                        queue.append((x + 1, y, island_cnt))
                    if y > 0:
                        queue.append((x, y - 1, island_cnt))
                    if y < len(board[0]) - 1:
                        queue.append((x, y + 1, island_cnt))
        for k, v in islands_surrounded.items():
            if v:
                for x, y in islands[k]:
                    board[x][y] = 'X'