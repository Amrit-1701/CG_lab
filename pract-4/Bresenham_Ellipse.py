import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# -----------------------------------
# Input
# -----------------------------------

xc = int(input("Enter center X: "))
yc = int(input("Enter center Y: "))
rx = int(input("Enter radius along X (rx): "))
ry = int(input("Enter radius along Y (ry): "))

points = []


# -----------------------------------
# 4-Way Symmetry
# -----------------------------------

def plot4(x, y):
    pts = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]

    for p in pts:
        if p not in points:
            points.append(p)


# -----------------------------------
# Bresenham Ellipse Algorithm
# -----------------------------------

x = 0
y = ry

rx2 = rx * rx
ry2 = ry * ry

# Initial decision parameter
d1 = ry2 - rx2 * ry + 0.25 * rx2

dx = 2 * ry2 * x
dy = 2 * rx2 * y


# -----------------------------------
# Region 1
# -----------------------------------

while dx < dy:

    plot4(x, y)

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


# -----------------------------------
# Region 2
# -----------------------------------

d2 = (
    ry2 * (x + 0.5) ** 2
    + rx2 * (y - 1) ** 2
    - rx2 * ry2
)

while y >= 0:

    plot4(x, y)

    if d2 > 0:
        y -= 1
        dy -= 2 * rx2

        d2 += rx2 - dy

    else:
        x += 1
        y -= 1

        dx += 2 * ry2
        dy -= 2 * rx2

        d2 += dx - dy + rx2


# -----------------------------------
# Sort points around ellipse
# -----------------------------------

import math

points.sort(
    key=lambda p: math.atan2(
        p[1] - yc,
        p[0] - xc
    )
)

# Close ellipse
points.append(points[0])

X = [p[0] for p in points]
Y = [p[1] for p in points]


# -----------------------------------
# Display
# -----------------------------------

plt.figure(figsize=(9, 9))

# Connect pixels
plt.plot(
    X,
    Y,
    '-o',
    linewidth=1.5,
    markersize=5
)

# Center
plt.scatter(
    xc,
    yc,
    color='red',
    s=100,
    zorder=5
)

plt.text(
    xc + 0.3,
    yc + 0.3,
    "Center"
)


# -----------------------------------
# 1 Unit Grid
# -----------------------------------

ax = plt.gca()

ax.xaxis.set_major_locator(
    MultipleLocator(1)
)

ax.yaxis.set_major_locator(
    MultipleLocator(1)
)

plt.grid(True)

# Equal unit scale
ax.set_aspect('equal')


# -----------------------------------
# Labels
# -----------------------------------

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title(
    "Bresenham Ellipse Drawing Algorithm"
)


# -----------------------------------
# Limits
# -----------------------------------

plt.xlim(
    xc - rx - 2,
    xc + rx + 2
)

plt.ylim(
    yc - ry - 2,
    yc + ry + 2
)

plt.show()