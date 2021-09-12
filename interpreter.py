# Copyright 2019 Leon Steinbach
import sys

# Valid commands with their quantity of parameters.
COMMANDS = {
    "LOAD": [1],
    "STORE": [1],
    "SETACC": [1],
    "MOVE": [2],
    "ADD": [2],
    "SUB": [2],
    "JUMP": [1, 2],
    "PRINT": [0]
}


def execute(command):
    """
    Executes a command with parameters given as string from the code file.
    """
    global ptr, acc, memory
    if not command or command[0] == "#":
        ptr += 1
        return

    commands = command.split(" ")
    if len(commands):
        if commands[0] not in COMMANDS.keys():
            print("Command not found <{0}> on line {1}".format(
                commands[0]), ptr)
            sys.exit(1)
        if len(commands) - 1 not in COMMANDS[commands[0]]:
            print("Command <{0}> on line {1}. Expected {2} parameters, \
                got {3}.".format(commands[0], ptr,
                                 COMMANDS[commands[0]], len(commands) - 1))
            sys.exit(1)

    if commands[0] == "LOAD":
        acc = memory[int(commands[1])]
        ptr += 1

    elif commands[0] == "STORE":
        memory[int(commands[1])] = acc
        ptr += 1

    elif commands[0] == "SETACC":
        acc = int(commands[1])
        ptr += 1

    elif commands[0] == "MOVE":
        memory[int(commands[2])] = memory[int(commands[1])]
        ptr += 1

    elif commands[0] == "ADD":
        memory[int(commands[1])] += memory[int(commands[2])]
        ptr += 1

    elif commands[0] == "SUB":
        memory[int(commands[1])] -= memory[int(commands[2])]
        ptr += 1

    elif commands[0] == "JUMP":
        if len(commands) == 2:
            ptr += int(commands[1])
        elif len(commands) == 3:
            jump = False
            if commands[1] == "=":
                jump = acc == 0
            elif commands[1] == "!=":
                jump = acc != 0
            elif commands[1] == "<":
                jump = acc < 0
            elif commands[1] == ">":
                jump = acc > 0
            elif commands[1] == "<=":
                jump = acc <= 0
            elif commands[1] == ">=":
                jump = acc >= 0

            if jump:
                ptr += int(commands[2])
            else:
                ptr += 1

    elif commands[0] == "PRINT":
        print(acc)
        ptr += 1


def main():
    global ptr, acc, memory
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <file.txt>")
        sys.exit(1)

    f = open(sys.argv[1], "r+")
    lines = [line.replace("\n", "") for line in f.readlines()]

    print("\nOutput\n")
    while ptr < len(lines):
        line = lines[ptr]
        execute(line)

    print("\nMemory\n")
    for i in range(len(memory)):
        print(str(i).zfill(len(str(len(memory)))), end=" ")
    print()
    for slot in memory:
        print(str(slot).zfill(len(str(len(memory)))), end=" ")
    print("\n")


if __name__ == "__main__":
    ptr = 0
    acc = 0
    memory = [0] * 32

    main()
