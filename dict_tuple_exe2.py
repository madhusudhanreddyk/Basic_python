def circle_calc(radius):
    area = 3.14*radius*radius
    circumference = 2*3.14*radius
    diameter = 2*radius
    return area , circumference , diameter


if __name__ == '__main__':
    r = input("Enter radius of the circle:")
    r = float(r)
    area , c, d = circle_calc(r)
    print(f" area : {area} , circumference : {c} , diameter : {d}")

    
