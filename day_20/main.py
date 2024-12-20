from collections import deque

MIN_TIME_SAVED = 100


def part_one():
    with open("input.txt") as file:
        racetrack = [list(line) for line in file.read().strip().splitlines()]
        rows, cols = len(racetrack), len(racetrack[0])
        startRow, startCol = next(
            (i, j) for i in range(rows) for j in range(cols) if racetrack[i][j] == "S"
        )
        startTime = 0
        queue = deque([(startRow, startCol, startTime)])
        visited = set()
        positionTimes = dict()
        while queue:
            currRow, currCol, currTime = queue.popleft()
            if (currRow, currCol) in visited:
                continue
            visited.add((currRow, currCol))
            positionTimes[(currRow, currCol)] = currTime
            directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if (
                    0 <= nextRow < rows
                    and 0 <= nextCol < cols
                    and racetrack[nextRow][nextCol] != "#"
                ):
                    queue.append((nextRow, nextCol, currTime + 1))
        numCheats = 0
        for (currRow, currCol), currTime in positionTimes.items():
            directions = {
                (-2, 0),
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -2),
                (0, -1),
                (0, 1),
                (0, 2),
                (1, -1),
                (1, 0),
                (1, 1),
                (2, 0),
            }
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if (nextRow, nextCol) in positionTimes:
                    timeSaved = (
                        positionTimes[(nextRow, nextCol)]
                        - currTime
                        - (abs(dr) + abs(dc))
                    )
                    if timeSaved >= MIN_TIME_SAVED:
                        numCheats += 1
        print(numCheats)


def part_two():
    with open("input.txt") as file:
        racetrack = [list(line) for line in file.read().strip().splitlines()]
        rows, cols = len(racetrack), len(racetrack[0])
        startRow, startCol = next(
            (i, j) for i in range(rows) for j in range(cols) if racetrack[i][j] == "S"
        )
        startTime = 0
        queue = deque([(startRow, startCol, startTime)])
        visited = set()
        positionTimes = dict()
        while queue:
            currRow, currCol, currTime = queue.popleft()
            if (currRow, currCol) in visited:
                continue
            visited.add((currRow, currCol))
            positionTimes[(currRow, currCol)] = currTime
            directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if (
                    0 <= nextRow < rows
                    and 0 <= nextCol < cols
                    and racetrack[nextRow][nextCol] != "#"
                ):
                    queue.append((nextRow, nextCol, currTime + 1))
        numCheats = 0
        for (currRow, currCol), currTime in positionTimes.items():
            for dr in range(-20, 21):
                for dc in range(-20 + abs(dr), 20 - abs(dr) + 1):
                    nextRow, nextCol = currRow + dr, currCol + dc
                    if (nextRow, nextCol) in positionTimes:
                        timeSaved = (
                            positionTimes[(nextRow, nextCol)]
                            - currTime
                            - (abs(dr) + abs(dc))
                        )
                        if timeSaved >= MIN_TIME_SAVED:
                            numCheats += 1
        print(numCheats)


if __name__ == "__main__":
    part_one()
    part_two()
