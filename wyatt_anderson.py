# CS 162
# Creating a Function to Find the Surface Area of a Rectangular Solid

def surface_area(length, width, height):
    return 2 * (rect_area(length, width) + (height * length) + (height * width))

