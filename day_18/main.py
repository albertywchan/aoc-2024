from collections import deque

ROWS = 71
COLS = 71
NUM_BYTES = 1024


def part_one():
    with open("input.txt") as file:
        bytes = set()
        for _ in range(NUM_BYTES):
            line = file.readline().strip()
            r, c = map(int, line.split(","))
            bytes.add((r, c))
        (
            startRow,
            startCol,
            endRow,
            endCol,
        ) = 0, 0, ROWS - 1, COLS - 1
        queue = deque([(startRow, startCol, 0)])
        visited = set()
        minSteps = -1
        while queue:
            currRow, currCol, currDistance = queue.popleft()
            if currRow == endRow and currCol == endCol:
                minSteps = currDistance
                break
            if (currRow, currCol) in visited:
                continue
            visited.add((currRow, currCol))
            directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
            for dr, dc in directions:
                nextRow, nextCol = currRow + dr, currCol + dc
                if (
                    0 <= nextRow < ROWS
                    and 0 <= nextCol < COLS
                    and (nextRow, nextCol) not in bytes
                ):
                    queue.append((nextRow, nextCol, currDistance + 1))
        print(minSteps)


def part_two():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        left, right = 0, len(lines) - 1
        firstByte = None
        while left <= right:
            minSteps = -1
            bytes = set()
            mid = (right + left) // 2
            for i in range(mid):
                line = lines[i].strip()
                r, c = map(int, line.split(","))
                bytes.add((r, c))
            (
                startRow,
                startCol,
                endRow,
                endCol,
            ) = 0, 0, ROWS - 1, COLS - 1
            queue = deque([(startRow, startCol, 0)])
            visited = set()
            minSteps = -1
            while queue:
                currRow, currCol, currDistance = queue.popleft()
                if currRow == endRow and currCol == endCol:
                    minSteps = currDistance
                    break
                if (currRow, currCol) in visited:
                    continue
                visited.add((currRow, currCol))
                directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
                for dr, dc in directions:
                    nextRow, nextCol = currRow + dr, currCol + dc
                    if (
                        0 <= nextRow < ROWS
                        and 0 <= nextCol < COLS
                        and (nextRow, nextCol) not in bytes
                    ):
                        queue.append((nextRow, nextCol, currDistance + 1))
            if minSteps == -1:
                right = mid - 1
            else:
                left = mid + 1
                firstByte = lines[mid]
        print(firstByte)


if __name__ == "__main__":
    part_one()
    part_two()
