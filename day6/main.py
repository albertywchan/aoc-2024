def part_one():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])
        for i in range(height):
            for j in range(width):
                if map[i][j] == "^":
                    startingPosY, startingPosX = i, j
                    break
        positionY, positionX = startingPosY, startingPosX
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        currDirectionIdx = 0
        currDirection = directions[currDirectionIdx]
        visitedPositions = set()
        uniquePositions = 0
        while (
            positionY >= 0
            and positionY < height
            and positionX >= 0
            and positionX < width
        ):
            if map[positionY][positionX] == "#":
                positionY = positionY - currDirection[0]
                positionX = positionX - currDirection[1]
                currDirectionIdx = (currDirectionIdx + 1) % 4
                currDirection = directions[currDirectionIdx]
            else:
                if (positionX, positionY) not in visitedPositions:
                    visitedPositions.add((positionX, positionY))
                    uniquePositions += 1
            positionY = positionY + currDirection[0]
            positionX = positionX + currDirection[1]
        print(uniquePositions)


def part_two():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])
        for i in range(height):
            for j in range(width):
                if map[i][j] == "^":
                    startingPositionY, startingPositionX = i, j
                    break
        positionY, positionX = startingPositionY, startingPositionX
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        currDirectionIdx = 0
        currDirection = directions[currDirectionIdx]
        guardRoute = set()
        while (
            positionY >= 0
            and positionY < height
            and positionX >= 0
            and positionX < width
        ):
            if map[positionY][positionX] == "#":
                positionY = positionY - currDirection[0]
                positionX = positionX - currDirection[1]
                currDirectionIdx = (currDirectionIdx + 1) % 4
                currDirection = directions[currDirectionIdx]
            else:
                guardRoute.add((positionY, positionX))
            positionY = positionY + currDirection[0]
            positionX = positionX + currDirection[1]
        obstructionPositions = 0
        for position in guardRoute:
            positionY, positionX = startingPositionY, startingPositionX
            obstructionPositionY, obstructionPositionX = position[0], position[1]
            currDirectionIdx = 0
            currDirection = directions[currDirectionIdx]
            visitedPositions = set()
            while (
                positionY >= 0
                and positionY < height
                and positionX >= 0
                and positionX < width
            ):
                if map[positionY][positionX] == "#" or (
                    positionY == obstructionPositionY
                    and positionX == obstructionPositionX
                ):
                    positionY = positionY - currDirection[0]
                    positionX = positionX - currDirection[1]
                    currDirectionIdx = (currDirectionIdx + 1) % 4
                    currDirection = directions[currDirectionIdx]
                else:
                    if (positionX, positionY, currDirectionIdx) in visitedPositions:
                        obstructionPositions += 1
                        break
                    else:
                        visitedPositions.add((positionX, positionY, currDirectionIdx))
                positionY = positionY + currDirection[0]
                positionX = positionX + currDirection[1]
        print(obstructionPositions)


if __name__ == "__main__":
    part_one()
    part_two()
