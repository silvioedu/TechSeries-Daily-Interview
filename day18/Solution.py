def find_cycle(graph):







graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {}
}

if __name__ == '__main__':
    print(find_cycle(graph))
    # False
    graph['c'] = graph
    print(find_cycle(graph))
    # True