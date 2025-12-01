import re
"""
rotating the dial L should be to lower numbers, R should be to upper numbers
11 -> R8 -> 19
wraps at 0/99

dial begins at 50

the password is the number of times the dial is left pointing at 0 after any rotation in the sequence

"""

def parse_line(line) -> tuple[str, int]:
    match = re.match(r"^(\D)(\d+)$", line)
    if match:
        dir = match.group(1) # "A"
        num = int(match.group(2))  # "123"
        return (dir, num)
def rotate(dir:str, amt:int, dial:int) -> int:
    new_dial = dial
    match dir.upper():
        case "R":
            new_dial = (dial + amt) % 100
        case "L":
            new_dial = (dial - amt) % 100
    
    return new_dial
            
def main():
    dial = 50
    password = 0
    with open(r"./inputs/day1", "r") as f:
       for line in f:
        dir, amt = parse_line(line)
        dial = rotate(dir, amt, dial)
        password = password + 1 if dial == 0 else password 
    print(password)

        


if __name__ == "__main__":
    main()