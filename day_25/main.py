def part_one():
    locks, keys = [], []
    with open("input.txt") as file:
        schematics = file.read().split("\n\n")
        for schematic in schematics:
            heights = [0] * 5
            schematic = schematic.splitlines()
            for i in range(1, len(schematic) - 1):
                for j in range(5):
                    if schematic[i][j] == "#":
                        heights[j] += 1
            if schematic[0] == "#####":
                locks.append(heights)
            else:
                keys.append(heights)
    keyLockPairs = 0
    for lock in locks:
        for key in keys:
            if all(pin1 + pin2 <= 5 for pin1, pin2 in zip(lock, key)):
                keyLockPairs += 1
    print(keyLockPairs)


def part_two():
    print("DONE")


if __name__ == "__main__":
    part_one()
    part_two()
