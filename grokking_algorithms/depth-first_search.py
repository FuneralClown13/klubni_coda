import copy


def dfs(graph: dict, start, goal):
    def dfs_x(graph: dict, start, goal, path=''):
        if start == goal:
            return path + goal
        while graph[start]:
            path += start
            return dfs_x(graph, graph[start].pop(0), goal, path)

    res = dfs_x(copy.deepcopy(graph), start, goal, path='')
    if res == None:
        return f'{start} =x=> {goal}'
    res_list = [i for i in res]
    return ' ===> '.join(res_list)


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

    print(dfs(ex_graph_dict, 'A', 'F'))
    print(dfs(ex_graph_dict, 'A', 'Z'))
    print(dfs(ex_graph_dict, 'A', 'L'))
    print(dfs(ex_graph_dict, 'L', 'B'))
