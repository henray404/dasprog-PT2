def last_man_standing(N, C):

    if N % 3 == 0:
        if C == 1:
            return "lili"
        return "lala"
    else:
        if C == 1:
            return "lala"

        return "lili"


N, C = input("input number of balls and and who first (1/2)").split(" ")
N = int(N)
C = int(C)
print(last_man_standing(N, C))
