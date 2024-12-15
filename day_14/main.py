from parse import search

ROWS = 103
COLS = 101


def part_one():
    with open("input.txt") as file:
        positions = []
        velocities = []
        numRobots = 0
        for line in file:
            position, velocity = line.strip().split()
            px, py = search("p={:d},{:d}", position)
            vx, vy = search("v={:d},{:d}", velocity)
            positions.append((py, px))
            velocities.append((vy, vx))
            numRobots += 1
        grid = [[0] * COLS for _ in range(ROWS)]
        for i in range(101):
            for j in range(numRobots):
                py, px = positions[j]
                vy, vx = velocities[j]
                if i > 0:
                    grid[py][px] -= 1
                    py, px = (py + vy) % ROWS, (px + vx) % COLS
                grid[py][px] += 1
                positions[j] = (py, px)
        quadrant1 = (0, ROWS // 2, 0, COLS // 2)
        quadrant2 = (0, ROWS // 2, COLS - COLS // 2, COLS)
        quadrant3 = (ROWS - ROWS // 2, ROWS, 0, COLS // 2)
        quadrant4 = (ROWS - ROWS // 2, ROWS, COLS - COLS // 2, COLS)
        safetyScore = 1
        for quadrant in {quadrant1, quadrant2, quadrant3, quadrant4}:
            numRobotsInQuad = 0
            rowStart, rowEnd, colStart, colEnd = quadrant
            for row in range(rowStart, rowEnd):
                numRobotsInQuad += sum(grid[row][colStart:colEnd])
            safetyScore *= numRobotsInQuad
        print(safetyScore)


def part_two():
    with open("input.txt") as file:
        positions = []
        velocities = []
        numRobots = 0
        for line in file:
            position, velocity = line.strip().split()
            px, py = search("p={:d},{:d}", position)
            vx, vy = search("v={:d},{:d}", velocity)
            positions.append((py, px))
            velocities.append((vy, vx))
            numRobots += 1
        grid = [[0] * COLS for _ in range(ROWS)]

        def print_grid(grid):
            for i in range(ROWS):
                print("".join(map(lambda x: "." if x == 0 else str(x), grid[i])))
            print("\n")

        maxRobotsInQuad = (0, 0)
        for i in range(ROWS * COLS):
            for j in range(numRobots):
                py, px = positions[j]
                vy, vx = velocities[j]
                if i > 0:
                    grid[py][px] -= 1
                    py, px = (py + vy) % ROWS, (px + vx) % COLS
                grid[py][px] += 1
                positions[j] = (py, px)
            quadrant1 = (0, ROWS // 2, 0, COLS // 2)
            quadrant2 = (0, ROWS // 2, COLS - COLS // 2, COLS)
            quadrant3 = (ROWS - ROWS // 2, ROWS, 0, COLS // 2)
            quadrant4 = (ROWS - ROWS // 2, ROWS, COLS - COLS // 2, COLS)
            for quadrant in {quadrant1, quadrant2, quadrant3, quadrant4}:
                numRobotsInQuad = 0
                rowStart, rowEnd, colStart, colEnd = quadrant
                for row in range(rowStart, rowEnd):
                    numRobotsInQuad += sum(grid[row][colStart:colEnd])
                if numRobotsInQuad > maxRobotsInQuad[0]:
                    maxRobotsInQuad = (numRobotsInQuad, i)
                    # print_grid(grid)
        elapsedSeconds = maxRobotsInQuad[1]
        print(elapsedSeconds)


if __name__ == "__main__":
    part_one()
    part_two()
