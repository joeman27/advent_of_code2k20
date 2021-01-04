from collections import deque

import re

class Edge():
    def __init__(self, head, tail, quantity):
        self.head = head
        self.tail = tail
        self.quantity = quantity


class NodeQuantities():
    def __init__(self, color: str):
        self.color = color
        self.edges = []

    def add_edge(self, node, quantity):
        edge = Edge(self, node, quantity)
        self.edges.append(edge)

    def __repr__(self):
        return f"{self.color}: {[(edge.tail.color, edge.quantity) for edge in self.edges]}\n"
    

def parse_colors(line):
    fragments = [fragment.strip() for fragment in re.split("contain|,", line)]
    node_color = " ".join(fragments[0].split(" ")[:2])
    colors_and_quantities = []
    for words in fragments[1:]:
        if not "no" in words:
            colors_and_quantities.append((" ".join(words.split(" ")[1:3]), int(words.split(" ")[0])))
    return (node_color, colors_and_quantities)

def construct_graph(lines):
    graph = {}
    for line in lines:
        (color, links) = parse_colors(line)
        node = NodeQuantities(color)
        if not color in graph:
            graph[color] = node
        for link in links:
            if not link[0] in graph:
                link_node = NodeQuantities(link[0])
                graph[link[0]] = link_node
            graph[color].add_edge(graph[link[0]], link[1])
    return graph

def bfs(origin):
    queue = deque([origin])
    visited = [origin]
    while len(queue) > 0:
        node = queue.popleft()
        for edge in node.edges:
            if not edge.tail in visited:
                visited.append(edge.tail)
                queue.append(edge.tail)
    return visited       

def sum_graph(origin):
    total = 0
    if len(origin.edges) == 0:
        total = 1
    else:
        for edge in origin.edges:
            total += sum_graph(edge) * edge.quantity
    return total

def dfs(origin):
    total = 0
    if len(origin.edges) == 0:
        total = 1
    else:
        for edge in origin.edges:
            total += sum_graph(edge) * edge.quantity
    return total