from collections import deque


def part_one():
    with open("input.txt") as file:
        secretNumbers = [int(line.strip()) for line in file]

        def mixAndPrune(value, secretNumber):
            res = value ^ secretNumber
            return res % 16777216

        for i in range(len(secretNumbers)):
            for _ in range(2000):
                secretNumber = secretNumbers[i]
                newSecretNumber = mixAndPrune(secretNumber << 6, secretNumber)
                newSecretNumber = mixAndPrune(newSecretNumber >> 5, newSecretNumber)
                newSecretNumber = mixAndPrune(newSecretNumber << 11, newSecretNumber)
                secretNumbers[i] = newSecretNumber
        print(sum(secretNumbers))


def part_two():
    with open("input.txt") as file:
        secretNumbers = [int(line.strip()) for line in file]
        sequences = set()
        buyerBananasMap = [dict() for _ in range(len(secretNumbers))]

        def mixAndPrune(value, secretNumber):
            res = value ^ secretNumber
            return res % 16777216

        for i in range(len(secretNumbers)):
            priceChanges = deque()
            for _ in range(2000):
                secretNumber = secretNumbers[i]
                newSecretNumber = mixAndPrune(secretNumber << 6, secretNumber)
                newSecretNumber = mixAndPrune(newSecretNumber >> 5, newSecretNumber)
                newSecretNumber = mixAndPrune(newSecretNumber << 11, newSecretNumber)
                onesDigit = newSecretNumber % 10
                priceChanges.append(onesDigit - secretNumber % 10)
                if len(priceChanges) == 4:
                    sequence = (
                        priceChanges[0],
                        priceChanges[1],
                        priceChanges[2],
                        priceChanges[3],
                    )
                    sequences.add(sequence)
                    if sequence not in buyerBananasMap[i]:
                        buyerBananasMap[i][sequence] = onesDigit
                    priceChanges.popleft()
                secretNumbers[i] = newSecretNumber
        mostBananas = 0
        for sequence in sequences:
            bananas = sum(buyer.get(sequence, 0) for buyer in buyerBananasMap)
            mostBananas = max(bananas, mostBananas)
        print(mostBananas)


if __name__ == "__main__":
    part_one()
    part_two()
