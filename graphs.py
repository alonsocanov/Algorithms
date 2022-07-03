

import collections
import heapq


def can_finish_course(num_courses: int, prerequisites: list) -> bool:
    pre_map = {i: [] for i in range(num_courses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        if pre_map[crs] == []:
            return True
        visited.add(crs)
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False

        visited.remove(crs)
        pre_map[crs] = []
        return True

    for crs in range(num_courses):
        if not dfs(crs):
            return False
    return True


def number_of_islands(grid: list[list[str]]):
    '''
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    '''
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(row, col):
        q = collections.deque()
        visit.add((row, col))
        q.append((row, col))
        while q:
            r, c = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visit):
                    q.append((row, col))
                    visit.add((row, col))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visit:
                bfs(row, col)
                islands += 1
    return islands


def valid_tree(n, edges):
    if not n:
        return True

    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()

    def dfs(i, prev):
        if i in visit:
            return False
        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and n == len(visit)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(dfs(n))

        return copy

    return dfs(node) if node else None


def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    max_area = 0
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visited:
            return 0
        visited.add((r, c))
        area = 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            area += dfs(r + dr, c + dc)
        return area

    for r in range(rows):
        for c in range(cols):
            max_area = max(max_area, dfs(r, c))
    return max_area


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    visit_pac, visit_atl = set(), set()

    def dfs(r, c, visit, prev_height):
        if ((r, c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < prev_height):
            return
        visit.add((r, c))
        neigh = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for dr, dc in neigh:
            dfs(dr, dc, visit, heights[r][c])

    for c in range(cols):
        dfs(0, c, visit_pac, heights[0][c])
        dfs(rows - 1, c, visit_atl, heights[rows-1][c])

    for r in range(rows):
        dfs(r, 0, visit_pac, heights[r][0])
        dfs(r, cols - 1, visit_atl, heights[r][cols - 1])

    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visit_pac and (r, c) in visit_atl:
                res.append([r, c])

    return res


def orangesRotting(self, grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = []
    time, fresh = 0, 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q and fresh:
        for i in range(len(q)):
            r, c = q.pop(0)
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1

        time += 1

    return time if not fresh else -1


def walls_and_gates(rooms: list[list[int]]):
    # write your code here

    q = []
    rows, cols = len(rooms), len(rooms[0])
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r, c))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    distance = 1
    while q:
        for _ in range(len(q)):
            r, c = q.pop(0)
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(rows) and col in range(cols) and rooms[row][col] == 2147483647:
                    rooms[row][col] = distance
                    q.append((row, col))
        distance += 1


def min_spanning_tree(points: list[list[int]]):
    N = len(points)
    adj = {i: [] for i in range(N)}
    for i in range(N):
        x, y = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x - x2) + abs(y - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Pim's algo
    visit = set()
    res = 0
    min_heap = [[0, 0]]
    while len(visit) < N:
        cost, i = heapq.heappop(min_heap)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neig_cost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(min_heap, [neig_cost, nei])
    return res


if __name__ == '__main__':
    array = [[0, 1], [0, 2], [1, 3], [0, 3], [1, 2], [2, 3]]
    print('The nodes are:', array)
    num_courses = 4
    print('Number of courses:', num_courses)
    can = can_finish_course(num_courses, array)
    print('Can finish all courses:', can)

    print("\nDetermine the number of islands")
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    print("The grid is:")
    print(grid)
    num_islands = number_of_islands(grid)
    print("the number of islands are:", num_islands)

    print("\nIs valid tree")
    tree = [[0, 1], [0, 2], [0, 3], [1, 4]]
    n = 5
    print("My edges are:", tree)
    print("Nodes:", n)
    is_tree = valid_tree(n, tree)
    print("It's a valid tree:", is_tree)

    print("\nWall and Gates")
    rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
    print("The rooms are:")
    print(rooms)
    walls_and_gates(rooms)
    print("The distance is:")
    print(rooms)

    print("\nPrims Algorithm")
    points = [[1, 0], [3, 4], [2, 6], [1, 2]]
    print("The point are:", points)
    distance = min_spanning_tree(points)
    print("the min distance connecting all point is:", distance)
