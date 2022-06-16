def can_finish_course(num_courses: int, prerequisites: list) -> bool:
    pre_map = {i: [] for i in range(num_courses + 1)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)
    print(pre_map)

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


if __name__ == '__main__':
    array = [[0, 1], [0, 2], [1, 3], [0, 3], [1, 2], [2, 3]]
    num_courses = 3
    print(can_finish_course(num_courses, array))
