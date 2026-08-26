import matplotlib.pyplot as plt

# Taking input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Simple DDA Algorithm
def Simple_DDA(x1, y1, x2, y2):

    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    m = dy / dx

    x = x1
    y = y1

    while x <= x2:

        x_points.append(round(x))
        y_points.append(round(y))

        x = x + 1
        y = y + m

    return x_points, y_points


# Generate points
x, y = Simple_DDA(x1, y1, x2, y2)


# Display output
plt.plot(x, y, marker='o')

plt.title("Simple DDA Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

# Show coordinates
for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i]},{y[i]})")

plt.show()