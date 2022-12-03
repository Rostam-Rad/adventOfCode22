from itertools import islice

def getInput(filename, n=3):
    with open(filename) as fp:
        for line in fp:
            yield [line] + list(islice(fp, n - 1))

def dayThreePartTwo(group):
    total = 0
    value = {}
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 0
    for j in range(1, 53):
        value[alpha[c]] = j
        c += 1

    used = []
    for i in [*group[0][:-1]]:
        if i in [*group[1]] and i in [*group[2]]:
            x = used.__contains__(i)
            used.append(i)
            if not x:
                total += value[i]

    return total


if __name__ == "__main__":
    answer = 0
    for lines in getInput("elf.txt"):
        answer += dayThreePartTwo(lines)
    print("Answer: ", answer)
