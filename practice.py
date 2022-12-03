def dayThree(ruckSack):


if __name__ == "__main__":
    f = open("elf.txt")
    file = f.read().splitlines()
    answer = 0
    for line in file:
        answer += dayTwo(line[0], line[2])
    print("answer = ", answer)

def dayTwo(i,j):
    score = 0
    value = {'X': 1, 'Y': 2, 'Z': 3}
    win = {"won": 6, "draw": 3, "lost": 0}
    lost = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    winGame = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    if(j == 'Y'): #You need to draw
        score += value[draw[i]]
        score += win["draw"]
    elif(j == 'X'): #You need to Lose
        score += value[lost[i]]
        score += win["lost"]
    elif (j == 'Z'): #You need to WIN
        score += value[winGame[i]]
        score += win["won"]

    return score