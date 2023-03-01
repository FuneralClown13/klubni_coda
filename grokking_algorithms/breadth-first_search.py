def bfs(graph: dict, start, goal):
    queue = [start]
    is_visited = []
    while queue:
        node = queue.pop(0)
        if node == goal:
            return path(is_visited, start, goal)
        for next_node in graph[node]:
            if next_node not in is_visited:
                is_visited.append((next_node, node))
                queue.append(next_node)
    return f'{start} =x=> {goal}'


def path(path_dict: list[tuple], start, goal):
    path = [goal]
    for i in path_dict:
        if goal == i[0]:
            goal = i[1]
            path.append(goal)
    path.append(start)
    return ' ===> '.join(reversed(path))


if __name__ == '__main__':
    ex_graph_dict = {
        'A': ['B', 'C', 'D', 'G', 'H'],
        'B': ['C', 'E', 'G', 'H', 'K', 'L'],
        'C': ['E', 'D', 'H', 'K', 'L'],
        'D': ['G', 'H'],
        'E': ['D', 'F', 'K', 'L'],
        'F': ['K'],
        'G': ['F'],
        'H': ['L'],
        'K': ['H', 'L'],
        'L': ['X'],
        'X': ['Y'],
        'Y': ['Z'],
        'Z': []
    }
    print(bfs(ex_graph_dict, 'A', 'F'))
    print(bfs(ex_graph_dict, 'A', 'Z'))
    print(bfs(ex_graph_dict, 'A', 'L'))
    print(bfs(ex_graph_dict, 'L', 'B'))
