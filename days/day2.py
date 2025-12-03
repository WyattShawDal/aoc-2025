"""
finding invalid ids

first id and last id seperated by a dash - 

invaid ids are ids which are made of a seqeunce o digits repeated twice

no digits have leading zeros

need track invalid ids for the password

an ID which is made of some sequence of digits repeated twice is invalid

so we need to

A. Identify the longest sequence of digits (none repeat).
B. Identify if the following sequences of digits repeat more than once. 

So, if we create a window looking N unique digits, and slide that until the sum of the digits changes?


123123123

[1 2 3]
[2 3 1]
[3 1 2]
[1 2 3]

ONLY fails if the whole id is the sequence

"""
import re

def is_invalid(num):
    s = str(num)
    #must be even for us to repeat a sequence
    lo_half = s[:len(s)//2]
    hi_half = s[len(s)//2:]
    if lo_half == hi_half:
        return num
    else:
        return 0

#sequence must repeat at least twice
def is_invalid_part2(num):
    s = str(num)
    #we need to have at least a duplicate, so len(s)//2
    for n in range(1, len(s)//2 + 1):
        #always true for 1, ie 1111, 22, etc.
        if (len(s) % n) == 0:
            #get the string up to length//n, for 1 this is the whole string
            val = s[:n]
            #repeat times
            if val*(len(s)//n) == s:
                print(num, "is invalid")
                return num
    return 0

def parse_entrys(ranges) -> int:
    #pattern must be repeated exactly twice
    password = 0
    for span in ranges:
        res = span.split("-")
        lo = int(res[0])
        hi = int(res[1])
        print(f" === got range {lo}, {hi} ===")
        for num in range(lo, hi+1):
            password += is_invalid_part2(num)
    return password




def part1():
    password = 0 
    with open("./inputs/day2", "r") as f:
        result = f.read()
    delim = r"[,]"
    ranges = re.split(delim, result)
    password = parse_entrys(ranges)
    print(password)

    pass

def part2():
    password = 0 
    with open("./inputs/day2", "r") as f:
        result = f.read()
    delim = r"[,]"
    ranges = re.split(delim, result)
    password = parse_entrys(ranges)
    print(password)
    pass

def main():
    # part1()
    part2()

if __name__ == "__main__":
    main()