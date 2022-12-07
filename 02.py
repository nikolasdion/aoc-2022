def opp_int(opp):
    match opp:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3


def us_int(us):
    match us:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3

def res_int(res):
    match res:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6


def us_from_res_opp(res, opp):
    if res == 3:
        return opp
    elif res == 0:
        us = (opp - 1) % 3
    elif res == 6:
        us = (opp + 1) % 3

    if us == 0:
        return 3
    else:
        return us 

def calculate_score_1(opp_char, us_char):
    opp = opp_int(opp_char)
    us = us_int(us_char)
    result = ((us - opp + 1) % 3) * 3  # 6 for win, 3 for draw, 0 for loss
    return result + us

def calculate_score_2(opp_char, res_char):
    opp = opp_int(opp_char)
    res = res_int(res_char)
    us = us_from_res_opp(res, opp)
    return res + us


def get_input():
    input = []
    with open("./02-input.txt") as file_in:
        for line in file_in:
            input.append((line[0], line[2]))
    return input


def solution_1():
    input = get_input()
    total_score = 0
    for match in input:
        total_score += calculate_score_1(match[0], match[1])
    return total_score

def solution_2():
    input = get_input()
    total_score = 0
    for match in input:
        total_score += calculate_score_2(match[0], match[1])
    return total_score


print(f"Solution for part 1 is {solution_1()}")
print(f"Solution for part 1 is {solution_2()}")
