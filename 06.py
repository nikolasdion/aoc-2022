with open("./06-input.txt") as file_in:
    for line in file_in:
        input = line


def is_all_unique(ls):
    return len(set(ls)) == len(ls)


def solution_1():
    end_index = 4
    while end_index < len(input):
        if is_all_unique((list(input[end_index - 4 : end_index]))):
            return end_index  # index 0 to index 1
        end_index += 1

def solution_2():
    end_index = 14
    while end_index < len(input):
        if is_all_unique((list(input[end_index - 14 : end_index]))):
            return end_index  # index 0 to index 1
        end_index += 1


print(f"Solution for part 1 is {solution_1()}")
print(f"Solution for part 2 is {solution_2()}")
