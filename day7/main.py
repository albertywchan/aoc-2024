def part_one():
    with open("input.txt") as file:

        def isTrueEquation(testValue, currCombination, remainingNumbers, currIdx):
            if currIdx == len(remainingNumbers) - 1:
                if currCombination + int(remainingNumbers[currIdx]) == testValue:
                    return True
                elif currCombination * int(remainingNumbers[currIdx]) == testValue:
                    return True
                else:
                    return False
            if currCombination >= testValue:
                return False
            return isTrueEquation(
                testValue,
                currCombination + int(remainingNumbers[currIdx]),
                remainingNumbers,
                currIdx + 1,
            ) or isTrueEquation(
                testValue,
                currCombination * int(remainingNumbers[currIdx]),
                remainingNumbers,
                currIdx + 1,
            )

        totalCalibrationResult = 0
        for line in file:
            numbers = line.strip().split()
            testValue = int(numbers[0].rstrip(":"))
            if isTrueEquation(testValue, 0, numbers, 1):
                totalCalibrationResult += testValue
        print(totalCalibrationResult)


def part_two():
    with open("input.txt") as file:

        def isTrueEquation(testValue, currCombination, remainingNumbers, currIdx):
            if currIdx == len(remainingNumbers) - 1:
                if currCombination + int(remainingNumbers[currIdx]) == testValue:
                    return True
                elif currCombination * int(remainingNumbers[currIdx]) == testValue:
                    return True
                elif int(str(currCombination) + remainingNumbers[currIdx]) == testValue:
                    return True
                else:
                    return False
            if currCombination >= testValue:
                return False
            return (
                isTrueEquation(
                    testValue,
                    currCombination + int(remainingNumbers[currIdx]),
                    remainingNumbers,
                    currIdx + 1,
                )
                or isTrueEquation(
                    testValue,
                    currCombination * int(remainingNumbers[currIdx]),
                    remainingNumbers,
                    currIdx + 1,
                )
                or isTrueEquation(
                    testValue,
                    int(str(currCombination) + remainingNumbers[currIdx]),
                    remainingNumbers,
                    currIdx + 1,
                )
            )

        totalCalibrationResult = 0
        for line in file:
            numbers = line.strip().split()
            testValue = int(numbers[0].rstrip(":"))
            if isTrueEquation(testValue, 0, numbers, 1):
                totalCalibrationResult += testValue
        print(totalCalibrationResult)


if __name__ == "__main__":
    part_one()
    part_two()
