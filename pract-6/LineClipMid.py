import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 50,10
xmax, ymax = 80,40


def inside(x, y):
    return xmin <= x <= xmax and ymin <= y <= ymax


def midpoint_clip(x1, y1, x2, y2):

    # If both points are inside
    if inside(x1, y1) and inside(x2, y2):
        return x1, y1, x2, y2

    # If both points are outside on same side
    if x1 < xmin and x2 < xmin:
        return None

    if x1 > xmax and x2 > xmax:
        return None

    if y1 < ymin and y2 < ymin:
        return None

    if y1 > ymax and y2 > ymax:
        return None

    # Repeat midpoint subdivision
    for i in range(50):

        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        # If first point is outside
        if not inside(x1, y1):

            if x1 < xmin and mx < xmin:
                x1, y1 = mx, my

            elif x1 > xmax and mx > xmax:
                x1, y1 = mx, my

            elif y1 < ymin and my < ymin:
                x1, y1 = mx, my

            elif y1 > ymax and my > ymax:
                x1, y1 = mx, my

            else:
                x1, y1 = mx, my

        # If second point is outside
        elif not inside(x2, y2):

            if x2 < xmin and mx < xmin:
                x2, y2 = mx, my

            elif x2 > xmax and mx > xmax:
                x2, y2 = mx, my

            elif y2 < ymin and my < ymin:
                x2, y2 = mx, my

            elif y2 > ymax and my > ymax:
                x2, y2 = mx, my

            else:
                x2, y2 = mx, my

        # Both points inside
        else:
            break

    if inside(x1, y1) or inside(x2, y2):
        return x1, y1, x2, y2

    return None


# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Clipping
result = midpoint_clip(x1, y1, x2, y2)

print("\nClipping Window:")
print("xmin =", xmin, "ymin =", ymin)
print("xmax =", xmax, "ymax =", ymax)

if result:
    print("\nLine Accepted")
    print("Clipped Line:")
    print("(", round(result[0], 2), ",", round(result[1], 2), ")")
    print("to")
    print("(", round(result[2], 2), ",", round(result[3], 2), ")")
else:
    print("\nLine Rejected")


# Plot
plt.figure(figsize=(7, 6))

# Window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]

plt.plot(window_x, window_y, "k-", label="Clipping Window")

# Original line
plt.plot([x1, x2], [y1, y2], "b--", label="Original Line")

# Clipped line
if result:
    plt.plot(
        [result[0], result[2]],
        [result[1], result[3]],
        "r-",
        linewidth=3,
        label="Clipped Line"
    )

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Midpoint Subdivision Line Clipping")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()