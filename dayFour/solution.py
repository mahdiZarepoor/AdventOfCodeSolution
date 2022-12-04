import re


def evaluate(ranges: list) -> int:
    # evaluate if second reange fully overlaps first range
    if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
        return 1

    # evaluate if first reange fully overlaps second range
    elif ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
        return 1

    return 0


def main():
    f = open("input", "r")
    counter = 0

    while True:
        line = f.readline()
        if line == "":
            # EOF , return the result
            print(counter)
            break

        # convert each line into a list with four element represent start and stop of two ranges
        ranges = [int(x) for x in re.split('-|,', line)]
        counter += evaluate(ranges)


if __name__ == "__main__":
    main()
