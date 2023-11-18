import math

class Circle():
    # Initializes a Circle object with the provided radius.
    def __init__(self, radius):      
        self.radius = radius

    # Calculates and returns the diameter of the circle.
    def diameter(self):              
        return 2 * self.radius
    
    # Calculates and returns the area of the circle.
    def area(self): 
        return math.pi * self.radius ** 2   

    # Calculates and returns the perimeter of the circle.
    def perimeter(self):
        return math.pi * 2 * self.radius

    # Displays the properties of the circle including its diameter, area, and perimeter.
    def circle_properties(self):
        print(f"- The diameter of the circle is {self.diameter()}")
        print(f"- The area of the circle is {self.area()}")
        print(f"- The perimeter of the circle is {self.perimeter()}")


# Main Program

# Ask the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Ensure that the radius is positive
while radius <= 0 :
    radius = float(input("Reenter the radius of the circle (must be positive): "))

# Create a Circle object using the entered radius
circle1 = Circle(radius)

# Display the properties of the circle including diameter, area, and perimeter
circle1.circle_properties()
