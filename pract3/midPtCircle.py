import matplotlib.pyplot as plt

# Input
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

points = []


def plot(x, y):
    pts = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for p in pts:
        if p not in points:
            points.append(p)


# Midpoint Circle Algorithm
x = 0
y = r
p = 1 - r

plot(x, y)

while x < y:
    x += 1

    if p < 0:
        p = p + 2 * x + 1
    else:
        y -= 1
        p = p + 2 * (x - y) + 1

    plot(x, y)


# Plotting
X = [i[0] for i in points]
Y = [i[1] for i in points]

plt.figure(figsize=(7,7))

plt.scatter(X, Y, s=50, color="black")

plt.grid(True)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Midpoint Circle Drawing Algorithm")

plt.gca().set_aspect("equal")

plt.xticks(range(min(X)-2, max(X)+3))
plt.yticks(range(min(Y)-2, max(Y)+3))

plt.show()