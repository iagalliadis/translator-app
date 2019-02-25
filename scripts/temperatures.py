temperatures = [10, -20, -289, 100]


def c_to_f(temperatures, filename):
    with open(filename, "a") as myfile:
        for temp in temperatures:
            if temp > -273.15:
                f = temp * 9 / 5 + 32
                myfile.write(str(f) + "\n")


c_to_f(temperatures, "temperatures.txt")
