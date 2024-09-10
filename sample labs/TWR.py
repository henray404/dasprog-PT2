def cat_jumps(numbers, b, c, index):
    for i in range(c):
        for i in range(b):
            numbers.insert(0, numbers.pop())

    result = [numbers[i] for i in index]
    return result


numbers = list(map(int, input("input the 7 number: ").split(" ")))
b = int(input("input number of the jump: "))
c = int(input("input many jump: "))
index = list(map(int, input("input the index: ").split(" ")))

output = cat_jumps(numbers, b, c, index)
for n in output:
    print(n)
