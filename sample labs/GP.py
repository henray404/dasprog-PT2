def can_jump(n, distances):
    for distance in distances:
        if distance > n:
            return "NO HE CAN'T"
    return "YES HE CAN"


N, A, B, C, D = input("input n and distance all the pillars").split(" ")
N = int(N)
A, B, C, D = int(A), int(B), int(C), int(D)
distance = [A, B, C, D]
print(can_jump(N, distance))
