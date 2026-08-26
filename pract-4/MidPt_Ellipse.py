import matplotlib.pyplot as plt

# -------- Input --------
xc = int(input("Enter center X: "))
yc = int(input("Enter center Y: "))
rx = int(input("Enter semi-major axis (rx): "))
ry = int(input("Enter semi-minor axis (ry): "))

points = []


# Plot four symmetric points
def plot(x, y):
    pts = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]

    for p in pts:
        if p not in points:
            points.append(p)


# -------- Midpoint Ellipse Algorithm --------

x = 0
y = ry

rx2 = rx * rx
ry2 = ry * ry

dx = 2 * ry2 * x
dy = 2 * rx2 * y

# Region 1
d1 = ry2 - (rx2 * ry) + (0.25 * rx2)

while dx < dy:
    plot(x, y)

    if d1 < 0:
        x += 1
        dx += 2 * ry2
        d1 += dx + ry2
    else:
        x += 1
        y -= 1
        dx += 2 * ry2
        dy -= 2 * rx2
        d1 += dx - dy + ry2

# Region 2
d2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

while y >= 0:
    plot(x, y)

    if d2 > 0:
        y -= 1
        dy -= 2 * rx2
        d2 += rx2 - dy
    else:
        y -= 1
        x += 1
        dx += 2 * ry2
        dy -= 2 * rx2
        d2 += dx - dy + rx2


# -------- Plot --------

X = [p[0] for p in points]
Y = [p[1] for p in points]

plt.figure(figsize=(7,7))

plt.scatter(X, Y, color="black", s=60)

# Connect points for better visualization
plt.plot(X, Y)

plt.grid(True)

plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")

plt.gca().set_aspect("equal")

plt.xticks(range(min(X)-2, max(X)+3))
plt.yticks(range(min(Y)-2, max(Y)+3))

plt.show()