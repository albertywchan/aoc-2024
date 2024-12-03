def part_one():
    with open("input.txt") as file:
        memory = file.read()
        counter = 0
        result = 0
        while counter < len(memory) - 4:
            if memory[counter : counter + 4] == "mul(":
                counter += 4
                num1 = ""
                while counter < len(memory) and memory[counter].isnumeric():
                    num1 += memory[counter]
                    counter += 1
                if counter < len(memory) and memory[counter] == ",":
                    counter += 1
                    num2 = ""
                    while counter < len(memory) and memory[counter].isnumeric():
                        num2 += memory[counter]
                        counter += 1
                    if counter < len(memory) and memory[counter] == ")":
                        result += int(num1) * int(num2)
            counter += 1
        print(result)


def part_two():
    with open("input.txt") as file:
        memory = file.read()
        counter = 0
        result = 0
        enabled = True
        while counter < len(memory):
            if (
                not enabled
                and counter + 4 < len(memory)
                and memory[counter : counter + 4] == "do()"
            ):
                counter += 4
                enabled = True
            if (
                enabled
                and counter + 7 < len(memory)
                and memory[counter : counter + 7] == "don't()"
            ):
                counter += 7
                enabled = False
            if (
                enabled
                and counter + 4 < len(memory)
                and memory[counter : counter + 4] == "mul("
            ):
                counter += 4
                num1 = ""
                while counter < len(memory) and memory[counter].isnumeric():
                    num1 += memory[counter]
                    counter += 1
                if counter < len(memory) and memory[counter] == ",":
                    counter += 1
                    num2 = ""
                    while counter < len(memory) and memory[counter].isnumeric():
                        num2 += memory[counter]
                        counter += 1
                    if counter < len(memory) and memory[counter] == ")":
                        result += int(num1) * int(num2)
            counter += 1
        print(result)


if __name__ == "__main__":
    part_one()
    part_two()
