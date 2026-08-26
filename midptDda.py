import matplotlib.pyplot as plt


# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Midpoint Algorithm
def Midpoint(x1, y1, x2, y2):

    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    d = dy - (dx / 2)

    x = x1
    y = y1

    x_points.append(x)
    y_points.append(y)

    while x < x2:

        x += 1

        if d < 0:
            d = d + dy

        else:
            y += 1
            d = d + dy - dx

        x_points.append(x)
        y_points.append(y)

    return x_points, y_points



# Generate points
x, y = Midpoint(x1, y1, x2, y2)


# Display output
plt.plot(x, y, marker='o')

plt.title("Midpoint Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

# Show coordinates
for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i]},{y[i]})")

plt.show()