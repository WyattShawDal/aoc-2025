import argparse

def find_whitespaces(lines):
    empty = []
    
    for col in range(len(lines[0])):
        is_empty = True
        for line in lines:
            if line[col] != ' ':
                is_empty = False
                break
        if is_empty:
            empty.append(col)
    return empty

def calc_value(nums, operator):
    if operator == '+':
        return sum(nums)
    elif operator == '*':
        product = 1
        for num in nums:
            product *= num
        return product

def part1(result):
    lines = result.splitlines()
    seperators = find_whitespaces(lines)
    start_col = None
    # find problem
    problem_ranges = []
    for idx in range(len(lines[0])):
        if start_col is None:
            start_col = idx
        if idx in seperators:
            problem_ranges.append((start_col, idx))
            start_col = None
    if start_col is not None:
        problem_ranges.append((start_col, len(lines[0])))

    total = 0
    for start, end in problem_ranges:
        problem_slice = []
        for line in lines:
            val = line[start:end].strip()
            problem_slice.append(int(val) if val.isdigit() else val)
        operator = problem_slice.pop()
        total += calc_value(problem_slice, operator)
       
    return total


def part2(result):
    lines = result.splitlines()
    max_len =  max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines]
    seperators = find_whitespaces(lines)
    start_col = None
    # find problem
    problem_ranges = []
    for idx in range(len(lines[0])):
        if start_col is None:
            start_col = idx
        if idx in seperators:
            problem_ranges.append((start_col, idx))
            start_col = None
    if start_col is not None:
        problem_ranges.append((start_col, len(lines[0])))
    #we have problem ranges, now we need to check for each column in the range, what the number is and save it
    #numbers are written write to left and vertically down
    #construct numbers
    total = 0
    for start, end in problem_ranges:
        nums = []
        for col in range(start, end):
            num_str = ''
            for row in range(len(lines)):
                char = padded[row][col]
                if char == '+' or char =='*':
                    operator = char
                if char.isdigit():
                    num_str += char
            if num_str != '':
                nums.append(int(num_str))
        total += calc_value(nums, operator)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC 2025 Day 4")
    parser.add_argument(
        "--part",
        type=int,
        choices=[1, 2],
        default=1,
        help="Specify which part of the challenge to run (1 or 2). Default is 1.",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Use example input data instead of the main input data.",

    )
    args = parser.parse_args()

    if args.example:
        with open("./inputs/day6_ex", "r") as f:
            result = f.read()
    else:
        with open("./inputs/day6", "r") as f:
            result = f.read()



    if args.part == 1:
        print(f"Part 1 Result: {part1(result)}")
    else:
        print(f"Part 2 Result: {part2(result)}")