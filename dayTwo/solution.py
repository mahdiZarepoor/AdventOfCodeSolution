# it is guaranteed that each line of input consists of two letter
# first one is either A B or C
# second one is either X Y or Z


def evaluate(opponent_shape: str, my_shape: str) -> int:
    score = 0
    if my_shape == "X":
        score += 1
        if opponent_shape == "A":
            score += 3
            return score
        elif opponent_shape == "B":
            return score
        else:
            score += 6
            return score

    elif my_shape == "Y":
        score += 2
        if opponent_shape == "A":
            score += 6
            return score
        elif opponent_shape == "B":
            score += 3
            return score
        else:
            return score

    else:
        score += 3
        if opponent_shape == "A":
            return score
        elif opponent_shape == "B":
            score += 6
            return score
        else:
            score += 3
            return score


f = open("input", "r")
total_score = 0

while True:
    line = f.readline()
    if line == "":
        # EOF , return the result
        print("you total score is : " + str(total_score))
        break

    total_score += evaluate(line[0], line[2])
