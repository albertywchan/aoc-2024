from collections import defaultdict


def part_one():
    with open("input.txt") as file:
        graph = defaultdict(list)
        for line in file:
            computer1, computer2 = line.strip().split("-")
            graph[computer1].append(computer2)
            graph[computer2].append(computer1)
        interconnectedComputers = set()
        for computer1, connections in graph.items():
            if computer1.startswith("t") and len(connections) >= 3:
                for i in range(len(connections) - 1):
                    computer2 = connections[i]
                    for j in range(i, len(connections)):
                        computer3 = connections[j]
                        if computer2 in graph[computer3]:
                            interconnectedComputers.add(
                                tuple(sorted((computer1, computer2, computer3)))
                            )
        numInterconnectedComputers = len(interconnectedComputers)
        print(numInterconnectedComputers)


def part_two():
    with open("input.txt") as file:
        graph = defaultdict(set)
        for line in file:
            computer1, computer2 = line.strip().split("-")
            graph[computer1].add(computer2)
            graph[computer2].add(computer1)

        cliques = []

        # Bron-Kerbosch algorithm
        def findMaxCliques(R, P, X):
            if not P and not X:
                cliques.append(R)
            for v in list(P):
                findMaxCliques(
                    R.union({v}), P.intersection(graph[v]), X.intersection(graph[v])
                )
                P.remove(v)
                X.add(v)

        findMaxCliques(set(), set(graph.keys()), set())
        maxClique = max(cliques, key=len)
        password = ",".join(sorted(maxClique))
        print(password)


if __name__ == "__main__":
    part_one()
    part_two()
