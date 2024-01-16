import math

# Constants
h = 960
k = 560
r = 200

# Number of points
num_points = 360

# Initialize lists to store x and y coordinates
x_coordinates = []
y_coordinates = []

# Generate the coordinates
for i in range(num_points):
    # Calculate the angle
    theta = 2 * math.pi * i / num_points
    
    # Calculate x and y coordinates using the equation
    x = h + r * math.cos(theta)
    y = k + r * math.sin(theta)
    
    # Append the coordinates to the lists
    x_coordinates.append(x)
    y_coordinates.append(y)

# Print the coordinates
print("LeftDown 1")
for x, y in zip(x_coordinates, y_coordinates):
    print(f"MoveTo {x}, {y}")
    print("Delay 10")
print("LeftUp 1")