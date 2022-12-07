input = []
with open("./03-input.txt") as file_in:
    for line in file_in:
        input.append(line)


def priority(item):
    o = ord(item)
    if o < 91:
        return o - 38
    else:
        return o - 96


def solution_1():
    total = 0
    for line in input:
        mid = int((len(line) / 2))
        first_items = line[:mid]
        second_items = line[mid:]
        for item in second_items:
            if item in first_items:
                total += priority(item)
                break
    return total


def solution_2():
    total = 0
    current_elf = 0  # index of elf in the current group we look at, either 0, 1, or 2

    for line in input:
        match current_elf:
            case 0:
                common_item = set()
                for item in line:
                    common_item.add(item)
            case 1:
                new_common_item = set()
                for item in common_item:
                    if item in line:
                        new_common_item.add(item)
                common_item = new_common_item
            case 2:
                for item in line:
                    if item in common_item:
                        total += priority(item)
                        break

        current_elf = (current_elf + 1) % 3

    return total


print(f"Solution for part 1 is {solution_1()}")
print(f"Solution for part 2 is {solution_2()}")
