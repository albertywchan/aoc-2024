import numpy as np
from parse import search


def part_one():
    with open("input.txt") as file:
        clawMachines = file.read().strip().split("\n\n")

    def dp(prizeRemaining, buttonA, buttonB, memo):
        if prizeRemaining[0] < 0 or prizeRemaining[1] < 0:
            return float("inf")
        elif prizeRemaining[0] == 0 and prizeRemaining[1] == 0:
            return 0
        else:
            if (prizeRemaining, buttonA, buttonB) not in memo:
                memo[(prizeRemaining, buttonA, buttonB)] = min(
                    dp(
                        (
                            prizeRemaining[0] - buttonA[0],
                            prizeRemaining[1] - buttonA[1],
                        ),
                        buttonA,
                        buttonB,
                        memo,
                    )
                    + 3,
                    dp(
                        (
                            prizeRemaining[0] - buttonB[0],
                            prizeRemaining[1] - buttonB[1],
                        ),
                        buttonA,
                        buttonB,
                        memo,
                    )
                    + 1,
                )
            return memo[(prizeRemaining, buttonA, buttonB)]

    allTokens = 0
    for clawMachine in clawMachines:
        for line in clawMachine.split("\n"):
            if line.startswith("Button"):
                button, X, Y = search("Button {}: X+{:d}, Y+{:d}", line)
                X, Y = map(int, [X, Y])
                if button == "A":
                    buttonA = (X, Y)
                else:
                    buttonB = (X, Y)
            else:
                X, Y = map(int, search("Prize: X={:d}, Y={:d}", line))
                prize = (X, Y)
        memo = dict()
        tokens = dp(prize, buttonA, buttonB, memo)
        if tokens != float("inf"):
            allTokens += tokens
    print(allTokens)


def part_two():
    with open("input.txt") as file:
        clawMachines = file.read().strip().split("\n\n")

    def solve(prize, buttonA, buttonB):
        A = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])
        b = np.array([prize[0], prize[1]])
        x = np.linalg.solve(A, b)
        buttonAPresses, buttonBPresses = round(x[0]), round(x[1])
        if (
            buttonA[0] * buttonAPresses + buttonB[0] * buttonBPresses == prize[0]
            and buttonA[1] * buttonAPresses + buttonB[1] * buttonBPresses == prize[1]
        ):
            return buttonAPresses * 3 + buttonBPresses
        else:
            return 0

    allTokens = 0
    for clawMachine in clawMachines:
        for line in clawMachine.split("\n"):
            if line.startswith("Button"):
                button, X, Y = search("Button {}: X+{:d}, Y+{:d}", line)
                X, Y = map(int, [X, Y])
                if button == "A":
                    buttonA = (X, Y)
                else:
                    buttonB = (X, Y)
            else:
                X, Y = map(
                    lambda n: int(n) + 10000000000000,
                    search("Prize: X={:d}, Y={:d}", line),
                )
                prize = (X, Y)
        allTokens += solve(prize, buttonA, buttonB)
    print(allTokens)


if __name__ == "__main__":
    part_one()
    part_two()
