

from collections import deque
from unicodedata import name
from urllib.request import proxy_bypass
import copy
from sympy import N


class Node():
    def __init__(self, name, pre=None, dist=None, visit=0):
        self.name = name
        self.pre = pre
        self.dist = dist
        self.visit = visit

    def __str__(self):
        return print(f' dist : {self.dist}')
        # return print(f'name : {self.name}; pre : {self.pre}; dist : {self.dist}; visit : {self.dist}')


def read_txt(filename):
    f = open(filename, encoding="ISO-8859-1")
    all_line = []
    for line in f:
        line = line.replace('\n', "")
        movie = line.split("/")
        all_line.append(movie)
    return deque(all_line)


def BFS(nodes, node_dict, stat_point, end_point):
    quene = []
    # print(nodes.index(stat_point))
    # print(nodes[nodes.index(stat_point)])
    all_nodes = {}

    for node in nodes:
        n = Node(name=node)
        n.dist = 1000000
        n.pre = -1
        n.visit = 0
        all_nodes[node] = n

    all_nodes[stat_point].visit = 1
    all_nodes[stat_point].dist = 0
    quene.append(all_nodes[stat_point])

    while (len(quene) != 0):
        u = quene[0].name
        quene.pop(0)
        for node in node_dict[u]:
            if (all_nodes[node].visit == 0):
                all_nodes[node].visit = 1
                all_nodes[node].dist = all_nodes[u].dist + 1
                all_nodes[node].pre = u
                quene.append(all_nodes[node])
                # all_nodes[node].__str__

                # We stop BFS when we find
                # destination.
                if (node == end_point):
                    return all_nodes

    return False  # no link


def finish_class(all_line):
    redundant_actors = deque()
    movies_dict = {}
    for line in all_line:
        movies_dict[line[0]] = line[1:]
        redundant_actors.extend(line[1:])
    actors_name = set(redundant_actors)
    actors_dict = {}
    for actor in actors_name:
        actors_dict[actor] = []
    for line in all_line:
        for actor in line[1:]:
            actors_dict[actor].append(line[0])
    # print(movies_dict.keys())

    return movies_dict, actors_dict


if __name__ == '__main__':

    all_line = read_txt('PopularCast.txt')
    movies_dict, actors_dict = finish_class(all_line)
    # movies_name = movies_dict.keys()

    node_dict = copy.deepcopy(movies_dict)
    node_dict.update(actors_dict)

    nodes = deque(node_dict.keys())
    # the_start_point = 'Bacon, Kevin'  # input
    # the_end_point = 'Pelish, Randy'  # input

    the_start_point = input(
        'Enter the start point. If enter "N", the start point will use "Bacon, Kevin" as defult : ')
    if the_start_point == 'N':
        the_start_point = 'Bacon, Kevin'  # input
    the_end_point = input(
        f'Enter the end point. You will get the KB-number and the link graph from {the_start_point} : ')

    all_nodes = BFS(nodes, node_dict, the_start_point, the_end_point)
    node = the_end_point
    quene = []
    if all_nodes:
        KB_number = all_nodes[node].dist
        while node != the_start_point:
            if node in movies_dict.keys():
                KB_number -= 1
            quene.append(node)
            node = all_nodes[node].pre
    else:
        print(
            f'There is no link between {the_start_point} and {the_end_point}')

    print(f'The Kevin-Bacon numbers of {the_end_point} : {KB_number}')

    print('link graph')
    quene.append(node)
    for node in quene:
        if node in movies_dict.keys():
            print(f' -> (link movie){node}')
        else:
            print(f'{node}')
