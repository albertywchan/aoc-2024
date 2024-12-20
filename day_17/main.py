from parse import search


def part_one():
    with open("input.txt") as file:
        registers, program = file.read().strip().split("\n\n")
        registers = registers.splitlines()
        A, B, C = map(lambda x: search("Register {}: {:d}", x)[1], registers)
        program = program.split()[1].split(",")
        program = list(map(int, program))

        def getComboOperand(operand):
            if operand <= 3:
                return operand
            elif operand == 4:
                return A
            elif operand == 5:
                return B
            elif operand == 6:
                return C

        PC = 0
        output = []
        while PC < len(program):
            jump = False
            opcode, operand = program[PC], program[PC + 1]
            if opcode == 0:
                operand = getComboOperand(operand)
                A = A >> operand
            elif opcode == 1:
                B = B ^ operand
            elif opcode == 2:
                operand = getComboOperand(operand)
                B = operand % 8
            elif opcode == 3:
                if A != 0:
                    jump = True
            elif opcode == 4:
                B = B ^ C
            elif opcode == 5:
                operand = getComboOperand(operand)
                output.append(str(operand % 8))
            elif opcode == 6:
                operand = getComboOperand(operand)
                B = A >> operand
            else:
                operand = getComboOperand(operand)
                C = A >> operand
            if jump:
                PC = operand
            else:
                PC += 2
        finalOutput = ",".join(output)
        print(finalOutput)


def part_two():
    with open("input.txt") as file:
        _, program = file.read().strip().split("\n\n")
        assert program == "Program: 2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0", "Wrong input file"
        program = program.split()[1].split(",")
        program = list(map(int, program))

        # Credit to HyperNeutrino (https://www.youtube.com/watch?v=y-UPxMAh2N8)
        def search(program, initialA):
            if len(program) == 0:
                return initialA >> 3
            for i in range(8):
                A = initialA + i
                B = A % 8
                B = B ^ 5
                C = A >> B
                B = B ^ 6
                B = B ^ C
                if B % 8 == program[-1]:
                    A = search(program[:-1], (A << 3))
                    if A != -1:
                        return A
            return -1

        lowestA = search(program, 0)
        print(lowestA)


if __name__ == "__main__":
    part_one()
    part_two()
