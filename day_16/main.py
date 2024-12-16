import heapq


def part_one():
    with open("input.txt") as file:
        maze = [line for line in file.read().strip().splitlines()]
        rows, cols = len(maze), len(maze[0])
        startRow, startCol, endRow, endCol = rows - 2, 1, 1, cols - 2
        startDirection = (0, 1)
        nodeDistances = dict()
        nodeDistances[(startRow, startCol, startDirection)] = 0
        unvisited = [(0, startRow, startCol, startDirection)]
        heapq.heapify(unvisited)
        while unvisited:
            currDistance, currRow, currCol, currDirection = heapq.heappop(unvisited)
            if currDistance > nodeDistances[(currRow, currCol, currDirection)]:
                continue
            cr, cc = currDirection
            directions = {(-1, 0), (0, 1), (1, 0), (0, -1)} - {(-cr, -cc)}
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if maze[nextRow][nextCol] != "#":
                    if (dr, dc) == currDirection:
                        nextDistance = currDistance + 1
                    else:
                        nextDistance = currDistance + 1001
                    if nextDistance < nodeDistances.get(
                        (nextRow, nextCol, (dr, dc)), float("inf")
                    ):
                        nodeDistances[(nextRow, nextCol, (dr, dc))] = nextDistance
                        heapq.heappush(
                            unvisited, (nextDistance, nextRow, nextCol, (dr, dc))
                        )
        score = min(
            nodeDistances.get((endRow, endCol, direction), float("inf"))
            for direction in {(-1, 0), (0, 1), (1, 0), (0, -1)}
        )
        print(score)


def part_two():
    with open("input.txt") as file:
        maze = [line for line in file.read().strip().splitlines()]
        rows, cols = len(maze), len(maze[0])
        startRow, startCol, endRow, endCol = rows - 2, 1, 1, cols - 2
        startDirection = (0, 1)
        startPath = [(startRow, startCol, startDirection)]
        bestPaths = []
        minScore = float("inf")
        nodeDistances = dict()
        nodeDistances[(startRow, startCol, startDirection)] = (0, startPath)
        unvisited = [(0, startRow, startCol, startDirection, startPath)]
        heapq.heapify(unvisited)
        while unvisited:
            currDistance, currRow, currCol, currDirection, currPath = heapq.heappop(
                unvisited
            )
            if currDistance > nodeDistances[(currRow, currCol, currDirection)][0]:
                continue
            if (currRow, currCol) == (endRow, endCol):
                if currDistance < minScore:
                    minScore = currDistance
                    bestPaths = [currPath]
                elif currDistance == minScore:
                    bestPaths.append(currPath)
                continue
            cr, cc = currDirection
            directions = {(-1, 0), (0, 1), (1, 0), (0, -1)} - {(-cr, -cc)}
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if maze[nextRow][nextCol] != "#":
                    if (dr, dc) == currDirection:
                        nextDistance = currDistance + 1
                    else:
                        nextDistance = currDistance + 1001
                    if (
                        nextDistance
                        <= nodeDistances.get(
                            (nextRow, nextCol, (dr, dc)), (float("inf"), [])
                        )[0]
                    ):
                        nextPath = [*currPath, (nextRow, nextCol, (dr, dc))]
                        nodeDistances[(nextRow, nextCol, (dr, dc))] = (
                            nextDistance,
                            nextPath,
                        )
                        heapq.heappush(
                            unvisited,
                            (nextDistance, nextRow, nextCol, (dr, dc), nextPath),
                        )
        numTiles = len({(row, col) for path in bestPaths for row, col, _ in path})
        print(numTiles)


if __name__ == "__main__":
    part_one()
    part_two()
