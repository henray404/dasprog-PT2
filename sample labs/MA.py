def car_pass(M, N, T):
    red_light = 20
    yellow_light = 5
    green_light = 60

    cycle_time = red_light + yellow_light + green_light

    car_passed = (T // cycle_time) * (green_light // 5)
    remaining_time = T % cycle_time

    if remaining_time > red_light + yellow_light:
        car_passed += (remaining_time - red_light - yellow_light) // 5

    total_cars = M + N + 1
    cars_left = total_cars - car_passed

    if cars_left <= 0:
        return "YES! 0"
    elif car_passed > M:
        return "YES! " + str(cars_left)
    else:
        return "NO! " + str(cars_left)


M, N, T = input("input M, N, T (front, back and time)").split(" ")
M = int(M)
N = int(N)
T = int(T)
print(car_pass(M, N, T))
