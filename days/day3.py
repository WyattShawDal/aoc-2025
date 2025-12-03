"""
Joltage is a value from 1 to 9 (and the inut)

the abteries are arranged into *banks*

each line of digits in my input needs corresponds to a single bank of batteries

for each bank we need to turn exactly two batteries

the joltage that the bank produes is equa to the number formed by the digits on the 
batteries I've truned on. For example a bank like 12345 with batteries 2 and 4 on then 
we have 24 jolts (can't reorder batteries, so we can't get 54 jolts for example)

In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, 
so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

"""


"""
couple notes:
there are duplicate numbers in a bank
we can't sort the banks
we can only turn on at most two

current idea is a two pointer approach 

1. Create L and R for the either side of the buffer
2. Check L R, in first example 91
3. Store 91 as max, maybe like (91, L, R) as a way of tracking
4. if L || R == 9 we don't need to move anymore, if L||R == 1 we should move
5. move lower of the two 



this solution is close but doesn't get the right value if R should not move always

what if instead of starting at either end we start them both at the left?

we have a couple condtions then:

1. L > R unless we reach the end
"""
def max_jolts(bank:str) -> int:
    r = 1 
    l = 0
    l = bank[l]
    r = bank[r]
    while r != len(bank):
        if l < bank[r] and r < len(bank) -1:
            l = r
            l = bank[l]
            #move r to the next value after l
            r = bank[r+1]
        elif bank[r] >= r:
            r = bank[r]
        r+=1
    num = int(l + r)
    return num

"""
now instead of two digits we need to track twelve.

lol.

so all but three numbers will be dropped, and need to be dropped in such a way as to minimize the best output



"""
def max_jolts(bank:str) -> int:
    r = 1 
    l = 0
    l = bank[l]
    r = bank[r]
    while r != len(bank):
        if l < bank[r] and r < len(bank) -1:
            l = r
            l = bank[l]
            #move r to the next value after l
            r = bank[r+1]
        elif bank[r] >= r:
            r = bank[r]
        r+=1
    num = int(l + r)
    return num

def part1(banks :list[str]) -> int:
    password = 0
    for bank in banks:
        password += max_jolts(bank)
    return password

def part2(banks :list[str]) -> int:
    password = 0
    for bank in banks:
        password += max_jolts(bank)
    return password



def part2():
    pass
def main():
    with open("./inputs/day3", "r") as f:
        result = f.read()
    banks = result.split("\n")
    print(banks)
    print(part1(banks))
    pass

if __name__ == "__main__":
    main()