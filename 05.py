import re
import copy

# [G]                 [D] [R]
# [W]         [V]     [C] [T] [M]
# [L]         [P] [Z] [Q] [F] [V]
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9
initial_stacks = [
    ["D", "T", "R", "B", "J", "L", "W", "G"],
    ["S", "W", "C"],
    ["R", "Z", "T", "M"],
    ["D", "T", "C", "H", "S", "P", "V"],
    ["G", "P", "T", "L", "D", "Z"],
    ["F", "B", "R", "Z", "J", "Q", "C", "D"],
    ["S", "B", "D", "J", "M", "F", "T", "R"],
    ["L", "H", "R", "B", "T", "V", "M"],
    ["Q", "P", "D", "S", "V"],
]

instructions = []  # move count from crater index to crater index

with open("./05-input.txt") as file_in:
    for line in file_in:
        match = re.search("move ([0-9]*) from ([0-9]*) to ([0-9]*)", line)
        if match is not None:
            instructions.append(
                (int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1)
            )


def solution_1():
    stacks = copy.deepcopy(initial_stacks)
    for inst in instructions:
        for _ in range(0, inst[0]):
            stacks[inst[2]].append(stacks[inst[1]].pop())

    answer = ""
    for stack in stacks:
        answer += stack[-1]
    return answer


def solution_2():
    stacks = copy.deepcopy(initial_stacks)
    for inst in instructions:
        moved_stack = []
        for _ in range(0, inst[0]):
            moved_stack.insert(0, stacks[inst[1]].pop())
        stacks[inst[2]].extend(moved_stack)

    answer = ""
    for stack in stacks:
        answer += stack[-1]
    return answer


print(f"Solution for part 1 is {solution_1()}")
print(f"Solution for part 2 is {solution_2()}")
