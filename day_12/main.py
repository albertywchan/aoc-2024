from collections import defaultdict, deque
from enum import Enum, auto


class Edge(Enum):
    TOP = auto()
    RIGHT = auto()
    BOTTOM = auto()
    LEFT = auto()


def part_one():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        rows, cols = len(map), len(map[0])
        visitedSet = set()

        def search(row, col):
            area, perimeter = 0, 0
            plant = map[row][col]
            queue = deque([(row, col)])
            while queue:
                currRow, currCol = queue.popleft()
                if (currRow, currCol) in visitedSet:
                    continue
                visitedSet.add((currRow, currCol))
                area += 1
                perimeter += 4
                directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
                for dr, dc in directions:
                    newRow = currRow + dr
                    newCol = currCol + dc
                    if (
                        0 <= newRow < rows
                        and 0 <= newCol < rows
                        and map[newRow][newCol] == plant
                    ):
                        if (newRow, newCol) in visitedSet:
                            perimeter -= 2
                        queue.append((newRow, newCol))
            return area, perimeter

        fencePrice = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visitedSet:
                    area, perimeter = search(r, c)
                    fencePrice += area * perimeter
        print(fencePrice)


def part_two():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        rows, cols = len(map), len(map[0])
        visitedSet = set()

        def search(row, col):
            area = 0
            edges = defaultdict(set)
            plant = map[row][col]
            queue = deque([(row, col)])
            while queue:
                currRow, currCol = queue.popleft()
                if (currRow, currCol) in visitedSet:
                    continue
                visitedSet.add((currRow, currCol))
                area += 1
                edges[(currRow, currCol)] = {
                    Edge.TOP,
                    Edge.RIGHT,
                    Edge.BOTTOM,
                    Edge.LEFT,
                }
                directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
                for dr, dc in directions:
                    newRow = currRow + dr
                    newCol = currCol + dc
                    if (
                        0 <= newRow < rows
                        and 0 <= newCol < rows
                        and map[newRow][newCol] == plant
                    ):
                        if (newRow, newCol) in visitedSet:
                            if (dr, dc) == (-1, 0):
                                edges[(currRow, currCol)].remove(Edge.TOP)
                                edges[(newRow, newCol)].remove(Edge.BOTTOM)
                            elif (dr, dc) == (0, 1):
                                edges[(currRow, currCol)].remove(Edge.RIGHT)
                                edges[(newRow, newCol)].remove(Edge.LEFT)
                            elif (dr, dc) == (1, 0):
                                edges[(currRow, currCol)].remove(Edge.BOTTOM)
                                edges[(newRow, newCol)].remove(Edge.TOP)
                            else:
                                edges[(currRow, currCol)].remove(Edge.LEFT)
                                edges[(newRow, newCol)].remove(Edge.RIGHT)
                        queue.append((newRow, newCol))

            sides = set()
            keys = list(edges.keys())
            for r, c in keys:
                candidateSides = edges[(r, c)]
                for side in candidateSides:
                    if (
                        side in {Edge.TOP, Edge.BOTTOM}
                        and side not in edges[(r, c - 1)]
                    ) or (
                        side in {Edge.RIGHT, Edge.LEFT}
                        and side not in edges[(r - 1, c)]
                    ):
                        sides.add((r, c, side))
            numSides = len(sides)
            return area, numSides

        fencePrice = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visitedSet:
                    area, sides = search(r, c)
                    fencePrice += area * sides
        print(fencePrice)


if __name__ == "__main__":
    part_one()
    part_two()
