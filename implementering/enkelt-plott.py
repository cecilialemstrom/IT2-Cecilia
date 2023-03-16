import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 2, 4, 6, 8, 10]

# plt.plot(x, y) # oppretter et plot
# plt.show() # viser plottet

# plott funksjonen f(x) = 3*x + 2 med x fra 0 til 5
# utfordring: bruk for-løkker

x1 = []
y1 = []

def f(x):
    return  3 * x + 2

for i in range(6):
    x1.append(i)
    y1.append(f(i))

plt.plot(x1,y1)
plt.scatter(x1, y1)
plt.show()

x2 = [0, 1, 2, 3, 4, 5]
y2 = []

for tall in x2:
    y2.append(3 * tall + 2)

plt.plot(x2, y2)
plt.show()