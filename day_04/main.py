def part_one():
    xmasAppearances = 0

    def search(i, j):
        nonlocal xmasAppearances
        if (
            j + 3 < width
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i][j + 1],
                    wordSearch[i][j + 2],
                    wordSearch[i][j + 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            j - 3 >= 0
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i][j - 1],
                    wordSearch[i][j - 2],
                    wordSearch[i][j - 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i + 3 < height
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i + 1][j],
                    wordSearch[i + 2][j],
                    wordSearch[i + 3][j],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i - 3 >= 0
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i - 1][j],
                    wordSearch[i - 2][j],
                    wordSearch[i - 3][j],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i - 3 >= 0
            and j + 3 < width
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i - 1][j + 1],
                    wordSearch[i - 2][j + 2],
                    wordSearch[i - 3][j + 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i + 3 < height
            and j + 3 < width
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i + 1][j + 1],
                    wordSearch[i + 2][j + 2],
                    wordSearch[i + 3][j + 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i + 3 < height
            and j - 3 >= 0
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i + 1][j - 1],
                    wordSearch[i + 2][j - 2],
                    wordSearch[i + 3][j - 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1
        if (
            i - 3 >= 0
            and j - 3 >= 0
            and "".join(
                [
                    wordSearch[i][j],
                    wordSearch[i - 1][j - 1],
                    wordSearch[i - 2][j - 2],
                    wordSearch[i - 3][j - 3],
                ]
            )
            == "XMAS"
        ):
            xmasAppearances += 1

    with open("input.txt") as file:
        wordSearch = []
        for line in file:
            wordSearch.append(line.strip())
        height, width = len(wordSearch), len(wordSearch[0])
        for i in range(height):
            for j in range(width):
                if wordSearch[i][j] == "X":
                    search(i, j)
    print(xmasAppearances)


def part_two():
    xmasAppearances = 0

    def search(i, j):
        nonlocal xmasAppearances
        if i - 1 >= 0 and i + 1 < height and j - 1 >= 0 and j + 1 < width:
            if (
                (wordSearch[i - 1][j - 1] == "M" and wordSearch[i + 1][j + 1] == "S")
                or (wordSearch[i - 1][j - 1] == "S" and wordSearch[i + 1][j + 1] == "M")
            ) and (
                (wordSearch[i + 1][j - 1] == "M" and wordSearch[i - 1][j + 1] == "S")
                or (wordSearch[i + 1][j - 1] == "S" and wordSearch[i - 1][j + 1] == "M")
            ):
                xmasAppearances += 1

    with open("input.txt") as file:
        wordSearch = []
        for line in file:
            wordSearch.append(line.strip())
        height, width = len(wordSearch), len(wordSearch[0])
        for i in range(height):
            for j in range(width):
                if wordSearch[i][j] == "A":
                    search(i, j)
    print(xmasAppearances)


if __name__ == "__main__":
    part_one()
    part_two()
