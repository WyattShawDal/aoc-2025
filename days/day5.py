import argparse
import bisect
"""
input ranges are inclusive as a list of ingredient ID ranges
3-5
10-14
16-20
12-18
(empty line)

1
5
8
11
17
32

so ingredients 3,4,5 are fresh

if a number in the second list doesn't fall into any range it is spoiled

Ranges can overlap, an ingredient is fresh if it is in any of the ranges

I'm currently thinking of essentially constructing a number line with some valid ranges, then just loop over the range

We just need to check each number of ingredient ID's for inclusivity to each range



"""
#takes in a range and the next range (sorted by start)
def overlaps(range1, range2):
    s1, e1 = range1
    s2, e2 = range2

    #check the ranges share an overlap
    if e1 >= s2:
        return (min(s1,s2), max(e1,e2))
    return None


def part1(ranges, ingredients):
    #construct ranges to check the inputs against
    sr = sorted(ranges, key=lambda x: x[0])
    pr = []
    current  = sr[0]
    for idx in range(1, len(sr)):
        n = overlaps(current, sr[idx])
        if n is not None:
            current  = n
        else:
            pr.append(current)
            current = sr[idx]
    pr.append(current)

    starts = [r[0] for r in pr]
    fc = 0
    for ingredient in ingredients:
        idx = bisect.bisect_right(starts, ingredient) - 1
        if idx >= 0 and pr[idx][0] <= ingredient <= pr[idx][1]:
             fc += 1

    return fc

def part2(ranges):
    sr = sorted(ranges, key=lambda x: x[0])
    pr = []
    current  = sr[0]
    for idx in range(1, len(sr)):
        n = overlaps(current, sr[idx])
        if n is not None:
            current  = n
        else:
            pr.append(current)
            current = sr[idx]
    pr.append(current)
    total_fresh_ids = 0 
    for r in pr:
        total_fresh_ids += (r[1] - r[0] + 1)

    return total_fresh_ids

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
        with open("./inputs/day5_ex", "r") as f:
            result = f.read()
    else:
        with open("./inputs/day5", "r") as f:
            result = f.read()


    raw = result.split("\n")
    ranges = []
    for line in raw:
        if line == "":
            break
        parts = line.split("-")
        ranges.append((int(parts[0]), int(parts[1])))
    ingredients = []
    for line in raw[len(ranges)+1:]:
        ingredients.append(int(line))
    if args.part == 1:
        print(f"Part 1 Result: {part1(ranges, ingredients)}")
    else:
        print(f"Part 2 Result: {part2(ranges)}")