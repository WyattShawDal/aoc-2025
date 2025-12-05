import argparse

"""
forklifts and only access a roll of paper if there are fewer than 4 roles of paper in the adjacent 8
positions.

Answer is how many rolls of paper can be accessed by a forklift

brute force:

check above , at , below rows, count @ if within distance = 1 of the toitlet paper we want to look at

grid is massive though, so this is likely really slow. Much smaller example input

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.


"""

def part1(grid) -> int:
    # [row][col]
    accessable = []
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0), (1, 1)]
    #loop from top to bottom, left to right
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            p_count = 0
            #if we find a paper
            if grid[row][col] == '@':
                #check all squares around the paper
                for offset in offsets:
                    new_row = row+offset[0]
                    new_col = col+offset[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        #if IB & paper
                        if grid[new_row][new_col] == '@':
                            p_count += 1
                    #if OOB don't count
                    else:
                        continue #can't count this cell (OOB)
                if p_count < 4:
                    accessable.append((row, col))
    return accessable


                


def part2(grid) -> int:
    num_removable = 0
    while True:
        #Calculate for current grid
        accessible = part1(grid)
        if len(accessible) == 0:
            break
        num_removable += len(accessible)
        #update our grid
        for row, col in accessible:
            grid[row][col] = '.'
    return num_removable
     
    

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
        with open("./inputs/day4_ex", "r") as f:
            result = f.read()
    else:
        with open("./inputs/day4", "r") as f:
            result = f.read()


    grid = [list(row) for row in result.split("\n")]
    if args.part == 1:
        print(f"Part 1 Result: {part1(grid)}")
    else:
        print(f"Part 2 Result: {part2(grid)}")