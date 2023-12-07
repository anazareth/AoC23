'''
Advent of Code 2023 Day 01
https://adventofcode.com/2023/day/1
AUTHOR: Alex Nazareth
DATE:   December 2023
Short description:
 - part 1: return sum of 2-digit numbers in each line
 -- 2 digits are the first and last digits in the line
 - part 2: digits include those spelled out in the line
 -- in cases like 'twone', we want 2 and 1 counted
'''

def part1(data):
    result = 0
    for row in data:
        ints = [r for r in row if r.isnumeric()]
        if len(ints) > 0:
            if len(ints) == 1:
                result += int(ints[0] + ints[0])
            else:
                result += int(''.join([ints[i] for i in [0,-1]]))
    return result

def part2(data):
    numname_to_num = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
                       'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
    data2 = []
    for row in data:
        for numname, num in numname_to_num.items():
            row = row.replace(numname, num)
        data2.append(row)
    return part1(data2)


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        rawdata = f.read().splitlines()

    print("Advent of Code 2023 Day 01")
    print("PART ONE: " + str(part1(rawdata)))
    print("PART TWO: " + str(part2(rawdata)))