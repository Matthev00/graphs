import sys
import argparse
from dijkstra import find_shortest_path, print_path


def read(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        graph = []
        for line in lines:
            line = line.replace('\n', '')
            tmp = []
            tmp[:0] = line
            graph.append(tmp)
    max_len = 0
    for line in graph:
        max_len = max(max_len, len(line))
    for line in graph:
        while len(line) < max_len:
            line.append(" ")
    return graph


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to txt file with graph')
    arguments = parser.parse_args(args[1:])
    G = read(arguments.path)

    # Debug
    # G = [['1', '1', '1', '1', '1', '1'],
    #      ['1', 'X', '4', '1', ' ', '1'],
    #      [' ', '4', ' ', '1', '1', '1'],
    #      [' ', '6', ' ', ' ', '1', ' '],
    #      [' ', '2', 'X', '4', '1', ' '],
    #      [' ', ' ', '1', '1', '1', ' ']]

    for line in G:
        print(line)

    print()
    
    x, y = find_shortest_path(G)
    z = print_path(G, y)
    for line in z:
        print(line)


if __name__ == "__main__":
    main(sys.argv)