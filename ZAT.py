def cylinder(color):

    contents = {
        'o': 'ammonia',
        'b': 'carbon moxide',
        'y': 'hydrogen',
        'g': 'oxygen'
    }

    color = color.lower()

    return contents.get(color, "conten unknown")


input_color = input("input the first leter of the cylinder")
print(cylinder(input_color))
