from collections import defaultdict


def part_one():
    with open("input.txt") as file:
        map = []
        trailheadScores = defaultdict(int)
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])

        def search(trailhead, row, col, prevHeight, visitedMap):
            if (row, col) not in visitedMap and int(map[row][col]) - prevHeight == 1:
                visitedMap.add((row, col))
                if map[row][col] == "9":
                    trailheadScores[trailhead] += 1
                neighbours = set()
                directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
                for dr, dc in directions:
                    if 0 <= row + dr < height and 0 <= col + dc < width:
                        neighbours.add((row + dr, col + dc))
                for nextRow, nextCol in neighbours:
                    search(trailhead, nextRow, nextCol, int(map[row][col]), visitedMap)

        for i in range(height):
            for j in range(width):
                if map[i][j] == "0":
                    visitedMap = set()
                    search((i, j), i, j, -1, visitedMap)

        trailheadScoresSum = sum(trailheadScores.values())
        print(trailheadScoresSum)


def part_two():
    with open("input.txt") as file:
        map = []
        trailheadRatings = defaultdict(int)
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])

        def search(trailhead, row, col, prevHeight):
            if int(map[row][col]) - prevHeight == 1:
                if map[row][col] == "9":
                    trailheadRatings[trailhead] += 1
                neighbours = set()
                directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
                for dr, dc in directions:
                    if 0 <= row + dr < height and 0 <= col + dc < width:
                        neighbours.add((row + dr, col + dc))
                for nextRow, nextCol in neighbours:
                    search(trailhead, nextRow, nextCol, int(map[row][col]))

        for i in range(height):
            for j in range(width):
                if map[i][j] == "0":
                    search((i, j), i, j, -1)

        trailheadRatingsSum = sum(trailheadRatings.values())
        print(trailheadRatingsSum)


if __name__ == "__main__":
    part_one()
    part_two()
