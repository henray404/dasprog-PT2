def calculate(data_usage):
    if data_usage <= 0:
        return "bad data."

    elif data_usage <= 1.0:
        return 250
    elif data_usage <= 2.0:
        return 500
    elif data_usage <= 5.0:
        return 1000
    elif data_usage <= 10.0:
        return 1500
    elif data_usage > 10.0:
        return 2000
    else:
        return "bad data."


try:
    data_usage = float(input("input data usage (in Gbbs): "))
    result = calculate(data_usage)
    print(f"charges: {result}")
except ValueError:
    print("invalid input.")
