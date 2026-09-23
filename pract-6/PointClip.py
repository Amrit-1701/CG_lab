import matplotlib.pyplot as plt

# Clipping window
xmin = 50
ymin = 10
xmax = 80
ymax = 40

# Input point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Point clipping
if xmin <= x <= xmax and ymin <= y <= ymax:
    print("\nPoint is INSIDE the window")
    accepted = True
else:
    print("\nPoint is OUTSIDE the window")
    accepted = False

# Draw clipping window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]

plt.figure(figsize=(7, 6))

plt.plot(window_x, window_y, "k-", label="Clipping Window")

# Plot point
if accepted:
    plt.plot(x, y, "go", markersize=10, label="Accepted Point")
else:
    plt.plot(x, y, "ro", markersize=10, label="Rejected Point")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Point Clipping")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()