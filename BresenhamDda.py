import matplotlib.pyplot as plt

# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Bresenham Algorithm
def Bresenham(x1, y1, x2, y2):

    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:

        x_points.append(x1)
        y_points.append(y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    return x_points, y_points


# Generate points
x, y = Bresenham(x1, y1, x2, y2)


# Display
plt.plot(x, y, marker='o')

plt.title("Bresenham Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i]},{y[i]})")

plt.show()