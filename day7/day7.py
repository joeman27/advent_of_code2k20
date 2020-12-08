from collections import deque

import re

class Node():
    def __init__(self, color: str):
        self.color = color
        self.links_to = []
        self.links_from = []

    def add_edge(self, node):
        self.links_to.append(node)
        node.links_from.append(self)

    def __repr__(self):
        return f"{self.color}: {[link.color for link in self.links_to]}\n"


def parse_colors(statement):
    fragments = re.split(r"\d", statement)
    colors = [" ".join(words.strip().split(" ")[:2]) for words in fragments]
    node_color = colors[0]
    links = colors[1:]
    return (node_color, links)

def construct_graph(lines):
    graph = {}
    for line in lines:
        (color, links) = parse_colors(line)
        node = Node(color)
        if not color in graph:
            graph[color] = node
        for link in links:
            if not link in graph:
                link_node = Node(link)
                graph[link] = link_node
            graph[color].add_edge(graph[link])
    return graph

def bfs(origin):
    queue = deque([origin])
    viewed = []
    while len(queue) > 0:
        node = queue.popleft()
        if node.color != "shiny gold":
            viewed.append(node.color)
        for link in node.links_from:
            if not link.color in viewed:
                viewed.append(link.color)
                queue.append(link)
    return viewed       

def part1():
    graph = {}
    with open("../files/day7", "r") as f:
        graph = construct_graph(f.readlines())
    ans = set(bfs(graph["shiny gold"]))
    print(ans)
    print(len(ans))

def part2():
    pass

    
if __name__ == "__main__":
    part1()
    part2()
    input("\nEnter to quit...")