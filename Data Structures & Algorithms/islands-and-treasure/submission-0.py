class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # started 3:20
        # BFS from each land square --> redundant
        #   - may have to repeat some squares
        # BFS from each treasure chest
        #   - only have to visit each square once
        #   - level order traversal from all chests simultaneously
        #   --> visits all squares 1 away from chest, then 2, etc.
        #   which nodes to visit?
        #   - if already visited: val < 2147483647
        #   - if it's a water cell: val = -1 ^by above
        #   - if the neighbor is within bounds
        from collections import deque

        q = deque()
        W, H = len(grid[0]), len(grid)

        # add all chests to queue
        for x in range(W):
            for y in range(H):
                if grid[y][x] == 0:
                    q.append((x, y))

        distance = 1
        while q:
            # num_nodes at a given distance
            num_nodes = len(q)
            for i in range(num_nodes):
                # get next node
                (x, y) = q.popleft()

                # explore neighbors
                neighbors = [
                    (x+1, y),
                    (x-1, y),
                    (x, y+1),
                    (x, y-1),
                ]

                for (x1, y1) in neighbors:
                    # not in bounds
                    if not (0 <= x1 < W and 0 <= y1 < H):
                        continue
                    # already visited or not a land cell
                    if grid[y1][x1] != 2147483647:
                        continue
                    grid[y1][x1] = distance
                    q.append((x1, y1))
            distance += 1
        

        