x1 = []
y1 = []

def f(x):
    return  2 * x - 3

for i in range(6):
    x1.append(i)
    y1.append(f(i))

plt.plot(x1,y1)
plt.scatter(x1, y1)
plt.show()
