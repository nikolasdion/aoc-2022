input = []
with open("./04-input.txt") as file_in:
    for line in file_in:
        elves = line.rstrip('\n').split(',')
        first_elf = elves[0].split('-')
        second_elf = elves[1].split('-')
        input.append(((int(first_elf[0]), int(first_elf[1])), (int(second_elf[0]), int(second_elf[1]))))

def solution_1():
    total = 0
    for assignment in input:
        if assignment[0][0] <= assignment [1][0] and assignment[0][1] >= assignment [1][1]:
            total += 1
        elif assignment[0][0] >= assignment [1][0] and assignment[0][1] <= assignment [1][1]:
            total += 1
    return total

def solution_2():
    total = 0
    for assignment in input:
        if assignment[0][0] >= assignment [1][0] and assignment[0][0] <= assignment [1][1]:
            total += 1
        elif assignment[0][1] >= assignment [1][0] and assignment[0][1] <= assignment [1][1]:
            total += 1
        elif assignment[1][0] >= assignment [0][0] and assignment[1][0] <= assignment [0][1]:
            total += 1
        elif assignment[1][1] >= assignment [0][0] and assignment[1][1] <= assignment [0][1]:
            total += 1
    return total

print(f"Solution for part 1 is {solution_1()}")
print(f"Solution for part 2 is {solution_2()}")