# initial arrangement of crates
crates = [
    ["J", "H", "P", "M", "S", "F", "N", "V"],
    ["S", "R", "L", "M", "J", "D", "Q"],
    ["N", "Q", "D", "H", "C", "S", "D", "B"],
    ["R", "S", "C", "L"],
    ["M", "V", "T", "P", "F", "B"],
    ["T", "R", "Q", "N", "C"],
    ["G", "V", "R"],
    ["C", "Z", "S", "P", "D", "L", "R"],
    ["D", "S", "J", "V", "G", "P", "B", "F"]
]

f = open("input", "r")
while True:
    line = f.readline().split(" ")

    # End Of File, break the loop and print the answer
    if len(line) == 1:
        print("top of stacks : ", end="")
        for i in crates:
            print(i[-1], end="")
        print()
        break

    number = int(line[1])
    src = int(line[3])
    dst = int(line[5])

    for i in range(number):
        # pop from src and push to destination
        crates[dst-1].append(crates[src-1].pop())
