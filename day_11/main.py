from collections import deque

PART_ONE_BLINKS = 25
PART_TWO_BLINKS = 75


def part_one():
    with open("input.txt") as file:
        line = file.readline().strip()
        stones = [int(x) for x in line.split()]

        def blink(stone):
            if stone == 0:
                return [1]
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                return [int(str(stone)[:half]), int(str(stone)[half:])]
            else:
                return [stone * 2024]

        queue = deque(stones)
        for _ in range(PART_ONE_BLINKS):
            for _ in range(len(queue)):
                stone = queue.popleft()
                transformation = blink(stone)
                for newStone in transformation:
                    queue.append(newStone)
        numStones = len(queue)
        print(numStones)


def part_two():
    with open("input.txt") as file:
        line = file.readline().strip()
        stones = [int(x) for x in line.split()]
        memo = dict()

        def blink(stone, blinksRemaining):
            if (stone, blinksRemaining) in memo:
                return memo[(stone, blinksRemaining)]
            if blinksRemaining == 0:
                return 1
            if stone == 0:
                length = blink(1, blinksRemaining - 1)
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                length = blink(int(str(stone)[:half]), blinksRemaining - 1) + blink(
                    int(str(stone)[half:]), blinksRemaining - 1
                )
            else:
                length = blink(stone * 2024, blinksRemaining - 1)
            memo[(stone, blinksRemaining)] = length
            return length

        numStones = sum(blink(stone, PART_TWO_BLINKS) for stone in stones)
        print(numStones)


if __name__ == "__main__":
    part_one()
    part_two()
