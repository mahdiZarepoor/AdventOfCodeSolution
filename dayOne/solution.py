f = open("input", "r")
greatest = 0
tmp = 0

while True:
    line = f.readline()
    if line == "":
        print("the answer is " + str(greatest))
        break

    if line == "\n":
        greatest = max(tmp, greatest)
        tmp = 0
        continue

    tmp += int(line)


# useful tips :
# f.readline() == "" means EOF in python
# f.readline() == "\n" is the specifier for different elves in this problems
