import matplotlib.pyplot as plt

# Function to plot 8 symmetric points
def plot_circle_points(xc, yc, x, y, points):
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

# Bresenham Circle Algorithm
def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

        x += 1

    return points

# -------- Main --------
xc = int(input("Enter center X: "))
yc = int(input("Enter center Y: "))
r = int(input("Enter radius: "))

points = bresenham_circle(xc, yc, r)

# Remove duplicate points
points = list(set(points))

X = [p[0] for p in points]
Y = [p[1] for p in points]

plt.figure(figsize=(7,7))
plt.scatter(X, Y, color="black", s=60)
plt.grid(True)

plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")

plt.gca().set_aspect('equal')

plt.xticks(range(min(X)-2, max(X)+3))
plt.yticks(range(min(Y)-2, max(Y)+3))

plt.show()