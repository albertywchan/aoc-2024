from collections import deque
from itertools import product

NUMERIC_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["X", "0", "A"]]
DIRECTIONAL_KEYPAD = [["X", "^", "A"], ["<", "v", ">"]]
DIRECTIONS = {(-1, 0), (0, 1), (1, 0), (0, -1)}
DIRECTION_MAP = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
PART_ONE_ROBOTS = 2
PART_TWO_ROBOTS = 25


def part_one():
    with open("input.txt") as file:

        def search(keypad, start, end):
            rows, cols = len(keypad), len(keypad[0])
            start = next(
                (i, j)
                for i in range(rows)
                for j in range(cols)
                if keypad[i][j] == start
            )
            end = next(
                (i, j) for i in range(rows) for j in range(cols) if keypad[i][j] == end
            )
            queue = deque([([], start)])
            shortestPaths = []
            shortestPathLength = float("inf")
            while queue:
                path, (cr, cc) = queue.popleft()
                if len(path) > shortestPathLength:
                    continue
                if (cr, cc) == end:
                    if len(path) < shortestPathLength:
                        shortestPaths = [[*path, "A"]]
                        shortestPathLength = len(path)
                    elif len(path) == shortestPathLength:
                        shortestPaths.append([*path, "A"])
                    continue
                for dr, dc in DIRECTIONS:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and keypad[nr][nc] != "X":
                        newPath = [*path, DIRECTION_MAP[(dr, dc)]]
                        queue.append((newPath, (nr, nc)))
            shortestPaths = list(map(lambda x: "".join(x), shortestPaths))
            return shortestPaths

        sumOfComplexities = 0
        for line in file:
            code = line.strip()
            sequences = []
            for i in range(len(code)):
                if i == 0:
                    sequences.append(search(NUMERIC_KEYPAD, "A", code[i]))
                else:
                    sequences.append(search(NUMERIC_KEYPAD, code[i - 1], code[i]))
            products = map(lambda x: "".join(x), product(*sequences))
            for _ in range(PART_ONE_ROBOTS):
                productsCopy = list(products)
                products = []
                for p in productsCopy:
                    sequences = []
                    for i in range(len(p)):
                        if i == 0:
                            sequences.append(search(DIRECTIONAL_KEYPAD, "A", p[i]))
                        else:
                            sequences.append(search(DIRECTIONAL_KEYPAD, p[i - 1], p[i]))
                    products.extend(map(lambda x: "".join(x), product(*sequences)))
                minLength = min(len(sequence) for sequence in products)
                products = [
                    sequence for sequence in products if len(sequence) == minLength
                ]
            complexity = minLength * int(code[:-1])
            sumOfComplexities += complexity
        print(sumOfComplexities)


def part_two():
    with open("input.txt") as file:
        memo = dict()

        def search(keypad, start, end):
            rows, cols = len(keypad), len(keypad[0])
            start = next(
                (i, j)
                for i in range(rows)
                for j in range(cols)
                if keypad[i][j] == start
            )
            end = next(
                (i, j) for i in range(rows) for j in range(cols) if keypad[i][j] == end
            )
            queue = deque([([], start)])
            shortestPaths = []
            shortestPathLength = float("inf")
            while queue:
                path, (cr, cc) = queue.popleft()
                if len(path) > shortestPathLength:
                    continue
                if (cr, cc) == end:
                    if len(path) < shortestPathLength:
                        shortestPaths = [[*path, "A"]]
                        shortestPathLength = len(path)
                    elif len(path) == shortestPathLength:
                        shortestPaths.append([*path, "A"])
                    continue
                for dr, dc in DIRECTIONS:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and keypad[nr][nc] != "X":
                        newPath = [*path, DIRECTION_MAP[(dr, dc)]]
                        queue.append((newPath, (nr, nc)))
            shortestPaths = list(map(lambda x: "".join(x), shortestPaths))
            return shortestPaths

        def dp(start, end, robotIdx):
            if (start, end, robotIdx) in memo:
                return memo[(start, end, robotIdx)]
            if robotIdx == 1:
                memo[(start, end, robotIdx)] = len(
                    search(DIRECTIONAL_KEYPAD, start, end)[0]
                )
            else:
                sequences = search(DIRECTIONAL_KEYPAD, start, end)
                minLength = float("inf")
                for sequence in sequences:
                    length = 0
                    for i in range(len(sequence)):
                        if i == 0:
                            length += dp("A", sequence[i], robotIdx - 1)
                        else:
                            length += dp(sequence[i - 1], sequence[i], robotIdx - 1)
                    minLength = min(length, minLength)
                memo[(start, end, robotIdx)] = minLength
            return memo[(start, end, robotIdx)]

        sumOfComplexities = 0
        for line in file:
            code = line.strip()
            sequences = []
            for i in range(len(code)):
                if i == 0:
                    sequences.append(search(NUMERIC_KEYPAD, "A", code[i]))
                else:
                    sequences.append(search(NUMERIC_KEYPAD, code[i - 1], code[i]))
            products = map(lambda x: "".join(x), product(*sequences))
            minLength = float("inf")
            for p in products:
                length = 0
                for i in range(len(p)):
                    if i == 0:
                        length += dp("A", p[i], PART_TWO_ROBOTS)
                    else:
                        length += dp(p[i - 1], p[i], PART_TWO_ROBOTS)
                minLength = min(length, minLength)
            complexity = minLength * int(code[:-1])
            sumOfComplexities += complexity
        print(sumOfComplexities)


if __name__ == "__main__":
    part_one()
    part_two()
