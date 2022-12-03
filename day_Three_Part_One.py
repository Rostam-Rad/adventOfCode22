def dayThreePartOne(ruckSack):
    total = 0
    value = {}
    firstCompartment, secondCompartment = ruckSack[:len(ruckSack) // 2], ruckSack[len(ruckSack) // 2:]
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 0
    for i in range(1, 53):
        value[alpha[c]] = i
        c += 1

    letters = []
    for i in firstCompartment:
        letters.append(i)
    for j in secondCompartment:
        if j in letters:
            total += value[j];
            letters = [l for l in letters if l != j]

    return total


if __name__ == "__main__":
    f = open("elf.txt")
    answer = 0
    for line in f:
        answer += dayThreePartOne(line)
    print("answer = ", answer)
