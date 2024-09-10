def number_check(N):
    if "4" in str(N):
        if "64" in str(N):
            return "failed"
        else:
            return "SEVER"

    else:
        return "UNITE"


N = int(input("input the number"))

if -100000 <= N <= 100000:
    print(number_check(N))
else:
    print("number out of constraints")
