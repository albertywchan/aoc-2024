from collections import defaultdict


def part_one():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])
        antennas = defaultdict(list)
        for row in range(height):
            for col in range(width):
                node = map[row][col]
                if node != ".":
                    antennas[node].append((row, col))
        antinodeMap = [[""] * width for _ in range(height)]
        uniqueLocations = 0
        for locations in antennas.values():
            for i in range(len(locations)):
                for j in range(len(locations)):
                    if i != j:
                        dy = locations[i][0] - locations[j][0]
                        dx = locations[i][1] - locations[j][1]
                        positionY, positionX = (
                            locations[i][0] + dy,
                            locations[i][1] + dx,
                        )
                        if (
                            0 <= positionY < height
                            and 0 <= positionX < width
                            and not antinodeMap[positionY][positionX]
                        ):
                            antinodeMap[positionY][positionX] = "#"
                            uniqueLocations += 1
        print(uniqueLocations)


def part_two():
    with open("input.txt") as file:
        map = []
        for line in file:
            map.append(line.strip())
        height, width = len(map), len(map[0])
        antennas = defaultdict(list)
        for row in range(height):
            for col in range(width):
                node = map[row][col]
                if node != ".":
                    antennas[node].append((row, col))
        antinodeMap = [[""] * width for _ in range(height)]
        uniqueLocations = 0
        for locations in antennas.values():
            for i in range(len(locations)):
                if not antinodeMap[locations[i][0]][locations[i][1]]:
                    antinodeMap[locations[i][0]][locations[i][1]] = "#"
                    uniqueLocations += 1
                for j in range(len(locations)):
                    if i != j:
                        dy = locations[i][0] - locations[j][0]
                        dx = locations[i][1] - locations[j][1]
                        positionY, positionX = (
                            locations[i][0] + dy,
                            locations[i][1] + dx,
                        )
                        while 0 <= positionY < height and 0 <= positionX < width:
                            if not antinodeMap[positionY][positionX]:
                                antinodeMap[positionY][positionX] = "#"
                                uniqueLocations += 1
                            positionY += dy
                            positionX += dx
        print(uniqueLocations)


if __name__ == "__main__":
    part_one()
    part_two()
