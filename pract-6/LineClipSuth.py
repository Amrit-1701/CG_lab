import matplotlib.pyplot as plt

# Window
xmin, ymin = -8, -4
xmax, ymax = 12, 8 

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def get_code(x, y):
    code = INSIDE

    if x < xmin:
        code = code | LEFT
    elif x > xmax:
        code = code | RIGHT

    if y < ymin:
        code = code | BOTTOM
    elif y > ymax:
        code = code | TOP

    return code


def cohen_sutherland(x1, y1, x2, y2):

    code1 = get_code(x1, y1)
    code2 = get_code(x2, y2)

    accept = False

    while True:

        # Both points inside
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Completely outside
        elif (code1 & code2) != 0:
            break

        # At least one point is outside
        else:

            if code1 != 0:
                code = code1
            else:
                code = code2

            # Find intersection with TOP
            if code & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            # Find intersection with BOTTOM
            elif code & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            # Find intersection with RIGHT
            elif code & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            # Find intersection with LEFT
            elif code & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace outside point
            if code == code1:
                x1, y1 = x, y
                code1 = get_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = get_code(x2, y2)

    if accept:
        return x1, y1, x2, y2
    else:
        return None


# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Clipping
result = cohen_sutherland(x1, y1, x2, y2)

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

# Clipping window
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
plt.title("Cohen-Sutherland Line Clipping")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()