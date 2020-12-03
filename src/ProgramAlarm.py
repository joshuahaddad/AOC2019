# Day 2 Program Alarm

# Reads the opcode file and changes the 1 and 2 addresses as specified by the noun/verb in the problem
def get_code(noun, verb):
    with open("../assets/opcode.txt", 'r') as f:
        instr = [int(i) for i in f.readlines()[0].split(",")]

    instr[1] = noun
    instr[2] = verb

    return instr


"""
Executes the opcode, default values take the noun and verb for part 1

Takes opcode in blocks of 4 instructions

Second and Third instructions are indexes of the instruction set whose values are added/multiplied

If the first instruction is 1, these values are added.  If 2, multiplied.
If the first instruction is 99, the program stops executing.
If the first instruction does not equal 1,2 or 99 the program had an error.

After computing the addition/multiplication the value is stored in the index of the final (fourth) instruction.

The output of the opcode is the value stored at the 0th element of the instructions
"""


def read_code(noun=12, verb=2):
    instr = get_code(noun, verb)
    for i in range(0, len(instr), 4):
        operation = instr[i]

        if operation == 99 and (operation != 1 or operation != 2):
            break

        a = instr[instr[i + 1]]
        b = instr[instr[i + 2]]

        value = a + b if operation == 1 else a * b

        instr[instr[i + 3]] = value

    return instr[0]


# Supplies different noun/verb combos to find the opcode output that equals a certain number (19690720 for my problem)
def run_code(objective=19690720):
    for noun in range(99):
        for verb in range(99):
            output = read_code(noun, verb)

            if output == objective:
                return noun, verb


Noun, Verb = run_code()
print(Noun, Verb)
print(100 * Noun + Verb)
