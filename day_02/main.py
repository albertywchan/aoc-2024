def part_one():
    with open("input.txt") as file:
        safeReports = 0
        for line in file:
            levels = [int(level) for level in line.split()]
            increasing = True
            if levels[0] > levels[1]:
                increasing = False
            elif levels[0] == levels[1]:
                continue
            safe = True
            for i in range(0, len(levels) - 1):
                if i > 0 and increasing and not (levels[i] < levels[i + 1]):
                    safe = False
                    break
                if i > 0 and not increasing and not (levels[i] > levels[i + 1]):
                    safe = False
                    break
                if abs(levels[i] - levels[i + 1]) > 3:
                    safe = False
                    break
            if safe:
                safeReports += 1
        print(safeReports)


def part_two():
    with open("input.txt") as file:
        safeReports = 0
        for line in file:
            levels = [int(level) for level in line.split()]
            increasing = True
            if levels[0] > levels[1]:
                increasing = False
            elif levels[0] == levels[1]:
                continue
            safe = True
            removed = False
            for i in range(0, len(levels) - 1):
                if i > 0 and increasing and not (levels[i] < levels[i + 1]):
                    if not removed:
                        removed = True
                    else:
                        safe = False
                        break
                if i > 0 and not increasing and not (levels[i] > levels[i + 1]):
                    if not removed:
                        removed = True
                    else:
                        safe = False
                        break
                if abs(levels[i] - levels[i + 1]) > 3:
                    if not removed:
                        removed = True
                    else:
                        safe = False
                        break
            if safe:
                safeReports += 1
        print(safeReports)


if __name__ == "__main__":
    part_one()
    part_two()
