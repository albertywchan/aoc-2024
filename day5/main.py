from collections import defaultdict


def part_one():
    with open("input.txt") as file:
        orderingRules = defaultdict(set)
        for line in file:
            if len(line.strip()) == 0:
                break
            pages = line.strip().split("|")
            orderingRules[pages[0]].add(pages[1])
        middlePageSum = 0
        for line in file:
            isCorrectlyOrdered = True
            update = line.strip().split(",")
            updateLength = len(update)
            for i in range(updateLength):
                for j in range(0, i):
                    if update[j] in orderingRules[update[i]]:
                        isCorrectlyOrdered = False
                        break
            if isCorrectlyOrdered:
                middlePageSum += int(update[updateLength // 2])
        print(middlePageSum)


def part_two():
    with open("input.txt") as file:
        orderingRules = defaultdict(set)
        for line in file:
            if len(line.strip()) == 0:
                break
            pages = line.strip().split("|")
            orderingRules[pages[0]].add(pages[1])
        middlePageSum = 0
        incorrectUpdates = []
        for line in file:
            isCorrectlyOrdered = True
            update = line.strip().split(",")
            updateLength = len(update)
            for i in range(updateLength):
                for j in range(0, i):
                    if update[j] in orderingRules[update[i]]:
                        isCorrectlyOrdered = False
                        break
            if not isCorrectlyOrdered:
                incorrectUpdates.append(update)
        for update in incorrectUpdates:
            updateLength = len(update)
            while True:
                swap = False
                for i in range(updateLength):
                    for j in range(0, i):
                        if update[j] in orderingRules[update[i]]:
                            update[i], update[j] = update[j], update[i]
                            swap = True
                if not swap:
                    break
            middlePageSum += int(update[updateLength // 2])
        print(middlePageSum)


if __name__ == "__main__":
    part_one()
    part_two()
