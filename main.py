import sys
import argparse

def read(path) :
    with open(path, 'r') as f:
        lines = f.readlines()
        graph = []
        for line in lines:
            line = line.replace('\n', '')
            tmp = []
            tmp[:0] = line
            graph.append(tmp)
    return graph

def main(args) :
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to txt file with graph')
    arguments = parser.parse_args(args[1:])
    G = read(arguments.path)
    for line in G:
        print(line)


if __name__ == "__main__":
    main(sys.argv)