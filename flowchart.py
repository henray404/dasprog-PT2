age = int(input("input age "))

if age > 59:
    status = input("input status")
    if status == "w":
        print("working senior")
    else:
        print("retired senior")

elif age > 20:
    print("adult")

elif age > 12:
    print("teenager")
else:
    print("child")
