

import collections


def can_finish_course(num_courses: int, prerequisites: list) -> bool:
    pre_map = {i: [] for i in range(num_courses + 1)}
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


if __name__ == '__main__':
    array = [[0, 1], [0, 2], [1, 3], [0, 3], [1, 2], [2, 3]]
    print('The nodes are:', array)
    num_courses = 3
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
