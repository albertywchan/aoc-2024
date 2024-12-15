def part_one():
    with open("input.txt") as file:
        mapInput, movementsInput = file.read().strip().split("\n\n")
        map = [list(line) for line in mapInput.splitlines()]
        rows, cols = len(map), len(map[0])
        movements = "".join(movementsInput.splitlines())
        movementsDict = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1),
        }
        robot = next(
            (r, c)
            for r in range(1, len(map) - 1)
            for c in range(1, len(map[0]) - 1)
            if map[r][c] == "@"
        )
        for movement in movements:
            dr, dc = movementsDict[movement]
            currRow, currCol = robot
            nextRow, nextCol = currRow + dr, currCol + dc
            if map[nextRow][nextCol] == "#":
                continue
            if map[nextRow][nextCol] == "O":
                checkRow, checkCol = nextRow + dr, nextCol + dc
                while map[checkRow][checkCol] != "#":
                    if map[checkRow][checkCol] == ".":
                        map[nextRow][nextCol] = "."
                        map[checkRow][checkCol] = "O"
                        break
                    checkRow += dr
                    checkCol += dc
            if map[nextRow][nextCol] == ".":
                map[currRow][currCol] = "."
                map[nextRow][nextCol] = "@"
                robot = (nextRow, nextCol)
        sumCoordinates = sum(
            100 * i + j for i in range(rows) for j in range(cols) if map[i][j] == "O"
        )
        print(sumCoordinates)


def part_two():
    with open("input.txt") as file:
        mapInput, movementsInput = file.read().strip().split("\n\n")
        map = [
            list(
                line.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            for line in mapInput.splitlines()
        ]
        rows, cols = len(map), len(map[0])
        movements = "".join(movementsInput.splitlines())
        movementsDict = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1),
        }
        robot = next(
            (r, c)
            for r in range(1, len(map) - 1)
            for c in range(1, len(map[0]) - 1)
            if map[r][c] == "@"
        )
        for movement in movements:
            dr, dc = movementsDict[movement]
            currRow, currCol = robot
            nextRow, nextCol = currRow + dr, currCol + dc
            stack = [(currRow, currCol)]
            seen = set()
            movedIntoWall = False
            boxes = dict()
            while stack:
                checkRow, checkCol = stack.pop()
                if (checkRow, checkCol) in seen:
                    continue
                seen.add((checkRow, checkCol))
                checkRow += dr
                checkCol += dc
                if map[checkRow][checkCol] == "#":
                    movedIntoWall = True
                    break
                elif map[checkRow][checkCol] == ".":
                    continue
                else:
                    stack.append((checkRow, checkCol))
                    boxes[(checkRow, checkCol)] = map[checkRow][checkCol]
                    if map[checkRow][checkCol] == "[":
                        stack.append((checkRow, checkCol + 1))
                        boxes[(checkRow, checkCol + 1)] = map[checkRow][checkCol + 1]
                    elif map[checkRow][checkCol] == "]":
                        stack.append((checkRow, checkCol - 1))
                        boxes[(checkRow, checkCol - 1)] = map[checkRow][checkCol - 1]
            if not movedIntoWall:
                for r, c in boxes.keys():
                    map[r][c] = "."
                for r, c in boxes.keys():
                    map[r + dr][c + dc] = boxes[(r, c)]
                map[currRow][currCol] = "."
                map[nextRow][nextCol] = "@"
                robot = (nextRow, nextCol)
        sumCoordinates = sum(
            100 * i + j for i in range(rows) for j in range(cols) if map[i][j] == "["
        )
        print(sumCoordinates)


if __name__ == "__main__":
    part_one()
    part_two()
