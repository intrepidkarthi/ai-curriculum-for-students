"""Grid shortest path using BFS.
0 = free, 1 = wall; moves in 4 directions. Return length or -1 if no path.
"""
from collections import deque
from typing import List

def shortest_path_len(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return -1
    q = deque([(0, 0, 0)])  # r, c, dist
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if r == m - 1 and c == n - 1:
            return d
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
