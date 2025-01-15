import math

def calc_quad() -> float:
    is_adding = True
    is_choosing = True

    width = 0
    length = 0
    while is_choosing:
        print("add/remove y/n")
        i = input()
        if i == "y":
            is_adding = True
            is_choosing = False
        elif i == "n":
            is_adding = False
            is_choosing = False

    is_choosing = True
    while is_choosing:
        print("enter width")
        i = input()
        width = float(i)
        is_choosing = False
    is_choosing = True
    while is_choosing:
        print("enter length")
        i = input()
        length = float(i)
        is_choosing = False
    if is_adding:
        return width * length
    else:
        return width * -length

def calc_tri() -> float:
    return calc_quad()/2

def calc_sphere() -> float:
    is_adding = True
    is_halved = False
    is_choosing = True

    radius = 0
    while is_choosing:
        print("add/remove y/n")
        i = input()
        if i == "y":
            is_adding = True
            is_choosing = False
        elif i == "n":
            is_adding = False
            is_choosing = False

    is_choosing = True
    while is_choosing:
        print("enter radius")
        i = input()
        radius = float(i)
        is_choosing = False

    is_choosing = True
    while is_choosing:
        print("enter is halved y/n")
        i = input()
        if i == "y":
            is_halved = True
            is_choosing = False
        elif i == "n":
            is_halved = False
            is_choosing = False

    if is_adding:
        if is_halved:
            return (radius**2 * math.pi) / 2
        else:
            return radius**2 * math.pi
    else:
        if is_halved:
            return (radius ** 2 * math.pi) / 2
        else:
            return radius ** 2 * math.pi

def main():
    area = 0
    calculating = True
    while calculating:
        print("current area: " + str(area))
        print("1 add/remove quadrilateral")
        print("2 add/remove triangles")
        print("3 add/remove sphere")
        print("press/remove enter to commence calculation")
        num = int(input())
        if num == 1:
            area += calc_quad()
        elif num == 2:
            area += calc_tri()
        elif num == 3:
            area += calc_sphere()
        else:
            print("commencing calculation")
            print(str(area))
            calculating = False
main()