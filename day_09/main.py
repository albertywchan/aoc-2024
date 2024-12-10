def part_one():
    with open("input.txt") as file:
        diskMap = file.readline().strip()
        compactedDiskMap = []
        for i, length in enumerate(diskMap):
            if i % 2 == 0:
                block = str(i // 2)
            else:
                block = "."
            for _ in range(int(length)):
                compactedDiskMap.append(block)
        left, right = 0, len(compactedDiskMap) - 1
        while left <= right:
            if compactedDiskMap[left] == ".":
                compactedDiskMap[left], compactedDiskMap[right] = (
                    compactedDiskMap[right],
                    compactedDiskMap[left],
                )
                left += 1
                while compactedDiskMap[right] == ".":
                    right -= 1
            else:
                left += 1
        checksum = 0
        for i in range(left):
            checksum += i * int(compactedDiskMap[i])
        print(checksum)


def part_two():
    with open("input.txt") as file:
        diskMap = file.readline().strip()
        compactedDiskMap = []
        for i, length in enumerate(diskMap):
            if i % 2 == 0:
                block = str(i // 2)
            else:
                block = "."
            for _ in range(int(length)):
                compactedDiskMap.append(block)
        right = len(compactedDiskMap) - 1
        blockSize = 0
        while right > 0:
            if compactedDiskMap[right] == ".":
                right -= 1
                continue
            blockSize = 0
            fileId = compactedDiskMap[right]
            while compactedDiskMap[right] == fileId:
                blockSize += 1
                right -= 1
            freeSpace = ["."] * blockSize
            left = 0
            while left < right:
                if (
                    compactedDiskMap[left] == "."
                    and compactedDiskMap[left : left + blockSize] == freeSpace
                ):
                    compactedDiskMap[left : left + blockSize] = compactedDiskMap[
                        right + 1 : right + 1 + blockSize
                    ]
                    compactedDiskMap[right + 1 : right + 1 + blockSize] = freeSpace
                    break
                left += 1
        checksum = 0
        for i, block in enumerate(compactedDiskMap):
            if block != ".":
                checksum += i * int(block)
        print(checksum)


if __name__ == "__main__":
    part_one()
    part_two()
