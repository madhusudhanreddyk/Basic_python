def calculate_area(dim1,dim2,shape="triangle"):
    if shape == "triangle":
        area = 1/2*dim1*dim2
    elif shape == "rectangle":
        area = dim1*dim2
    else:
        area = "i don't know"
    return area
tri_angle = calculate_area(1,1,"triangle")
print(tri_angle)
rect_angle = calculate_area(1,2,"rectangle")
print(rect_angle)

