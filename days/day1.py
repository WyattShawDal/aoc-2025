import re
"""
rotating the dial L should be to lower numbers, R should be to upper numbers
11 -> R8 -> 19
wraps at 0/99

dial begins at 50

the password is the number of times the dial is left pointing at 0 after any rotation in the sequence

new rule, we need to count any time the dial passes 0, not just when we end on it.

we know the dials initial position, if we rotate left and end higher we passed 0, if we rotate right and end lower we passed 0, if we're rotated > current but now == current, we passed 0

more formally

case 1: Given L direction, if new_dial > cur_dial, passed 0 count++
case 2: Given R direction ,if new_dial < cur_dial, passed 0 count++
case 3: Given L | R direction, if new_dial == cur_dial, passed 0 count++

how do we handle many rotations?

we could break the rotations up into batches of 100 ?, well a rotation of 100 will result in ending in the same location, right?
so we just need to figure out how many 100s fit in the rotation, and then use the remainder for case 1/2

"""

def parse_line(line) -> tuple[str, int]:
    match = re.match(r"^(\D)(\d+)$", line)
    if match:
        dir = match.group(1).upper() # "A"
        num = int(match.group(2))  # "123"
        return (dir, num)
def rotate(dir:str, amt:int, dial:int) -> int:
    new_dial = dial
    match dir:
        case "R":
            new_dial = (dial + amt) % 100
        case "L":
            new_dial = (dial - amt) % 100
    
    return new_dial

def full_rotation(old_dial, dir, amt):
    incr = 0
    rem = 0
    #will loop back to original location
    if(amt > 100):
        #how many times do we loop to original location
        incr = amt//100
        #what's left
        rem = amt % 100
    else:
        rem = amt
    #rotate the dial using remainder
    new_dial = rotate(dir, rem, old_dial)
    #Looped over 0 and ended at a higher value
    return new_dial, incr

def update_password(old, new, dir):
    incr = 0
    #if we started at 0, and rotation left or right does not count
    if old == 0:
        return 0
    elif new >= old and dir == "L" and old != 0:
        incr += 1
    #Looped over 0 and ended at a lower value
    elif new <= old and dir == "R":
        incr += 1
    elif new == 0:
        incr += 1
    return incr
            
def main():
    dial = 50
    password = 0
    with open(r"./inputs/day1", "r") as f:
       for line in f:
        dir, amt = parse_line(line)
        #perform rotation tracking the number of rotations around the dial
        new_dial, num_turns = full_rotation(dial, dir, amt)
        #add number of full rotations (require passing 0)
        password += num_turns
        #figure out password based on final position
        password += update_password(dial, new_dial, dir)
        dial = new_dial


    print(password)

        


if __name__ == "__main__":
    main()