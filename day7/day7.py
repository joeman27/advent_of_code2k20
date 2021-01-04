import node
import node_quantities

def part1():
    graph = {}
    with open("../files/day7", "r") as f:
        graph = node.construct_graph(f.readlines())
    ans = node.bfs(graph["shiny gold"])
    print(ans)
    print(len(ans))

def part2():
    graph = {}
    with open("../files/day7", "r") as f:
        graph = node_quantities.construct_graph(f.readlines())
    successors = node_quantities.bfs(graph["shiny gold"])
    for node in successors:
        for 

    
if __name__ == "__main__":
    part1()
    part2()
    input("\nEnter to quit...")