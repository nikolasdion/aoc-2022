def solution_1():
    max_cal = 0
    with open("./01-input.txt") as file_in:
        current_elf = 0
        for line in file_in:
            if line == "\n":
                if current_elf > max_cal:
                    max_cal = current_elf
                current_elf = 0
            else:
                current_elf += int(line)

    print(f'The answer is {max_cal}');

def new_top_three(current_top_three, num):
    if num < current_top_three[2]:
        return current_top_three
    elif num < current_top_three[1]:
        return [current_top_three[0], current_top_three[1], num]
    elif num < current_top_three[0]:
        return [current_top_three[0], num, current_top_three[1]]
    else:
        return [num, current_top_three[0], current_top_three[1]]


def solution_2():
    top_three = [0, -1, -2]
    with open("./01-input.txt") as file_in:
        current_elf = 0
        for line in file_in:
            if line == "\n":
                top_three = new_top_three(top_three, current_elf)
                current_elf = 0
            else:
                current_elf += int(line)

    print(f'The answer is {sum(top_three)}');
    
solution_1()
solution_2()