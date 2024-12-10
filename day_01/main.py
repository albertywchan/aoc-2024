def part_one():
    with open("input.txt") as file:
        leftList, rightList = [], []
        for line in file:
            locations = line.split()
            leftList.append(int(locations[0]))
            rightList.append(int(locations[1]))
        leftList.sort()
        rightList.sort()
        totalDistance = 0
        for l, r in zip(leftList, rightList):
            totalDistance += abs(l - r)
        print(totalDistance)


def part_two():
    with open("input.txt") as file:
        leftList, rightList = [], []
        locationDict = dict()
        for line in file:
            locations = line.split()
            leftList.append(int(locations[0]))
            rightList.append(int(locations[1]))
            locationDict[int(locations[1])] = locationDict.get(int(locations[1]), 0) + 1
        similarityScore = 0
        for location in leftList:
            similarityScore += location * locationDict.get(location, 0)
        print(similarityScore)


if __name__ == "__main__":
    part_one()
    part_two()
