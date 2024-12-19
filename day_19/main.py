def part_one():
    with open("input.txt") as file:
        patterns, designs = file.read().split("\n\n")
        patterns = set(map(lambda x: x.strip(), patterns.split(",")))
        designs = designs.splitlines()
        memo = dict()

        def dp(design):
            if not design:
                return True
            if design in memo:
                return memo[design]
            possible = False
            for pattern in patterns:
                patternLength = len(pattern)
                if design[:patternLength] == pattern:
                    if dp(design[patternLength:]):
                        possible = True
                        break
            memo[design] = possible
            return memo[design]

        possibleDesigns = sum(1 for design in designs if dp(design))
        print(possibleDesigns)


def part_two():
    with open("input.txt") as file:
        patterns, designs = file.read().split("\n\n")
        patterns = set(map(lambda x: x.strip(), patterns.split(",")))
        designs = designs.splitlines()
        memo = dict()

        def dp(design):
            if not design:
                return 1
            if design in memo:
                return memo[design]
            differentWays = 0
            for pattern in patterns:
                patternLength = len(pattern)
                if design[:patternLength] == pattern:
                    differentWays += dp(design[patternLength:])
            memo[design] = differentWays
            return memo[design]

        differentWays = sum(dp(design) for design in designs)
        print(differentWays)


if __name__ == "__main__":
    part_one()
    part_two()
