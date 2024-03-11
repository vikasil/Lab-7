import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import time


'''

arr=[randint(0,100) for _ in range(10**6)]
arr2=[randint(0,100) for _ in range(10**6)]
time.start = time.perf_counter()
result = [arr[i]*arr2[i] for i in range(10**6)]
time.end = time.perf_counter()
print("время выполнения операции поэлементного перемножения стандартных списков", time.end-time.start)

time.start = time.perf_counter()
result = np.multiply(np.array(arr),np.array(arr2))
time.end = time.perf_counter()
print("время выполнения операции поэлементного перемножения массивов NumPy", time.end-time.start)
'''



'''fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()'''
'''arr = pd.read_csv('data2.csv')
plt.hist(arr["Solids"], bins=20, label="a")

plt.show()
'''
arr = pd.read_csv('data2.csv')
plt.figure(1)
plt.hist(arr["Solids"], bins=20)
plt.title("histogram")
plt.xlabel("Solids")
plt.ylabel("quantity")
plt.show()

plt.figure(2)
plt.hist(arr["Solids"], bins=20, color="green", density=True)
plt.title("histogram2")
plt.xlabel("Solids")
plt.ylabel("quantity")
plt.show()
'''
def tableLoad():
    arr = np.genfromtxt('voltage.csv', delimiter=',')
    time = arr[:100,0]
    time = time[:,np.newaxis]
    curr = arr[:100,1]
    curr = curr[:,np.newaxis]
    volt = arr[:100,2]
    volt = volt[:,np.newaxis]

    plt.plot(time, curr * 50, 'b', time, volt, 'r')
    plt.show()


def hist():
    arr = np.genfromtxt('test.csv', delimiter=',')
    arr = arr[1:]
    daysInYear = 365.25

    age = np.int_(arr[:,1] / daysInYear)

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.hist(age, 100, (50, 60))
    ax.grid()
    plt.show()


def plot3d():
    np.random.seed(40)
    xs = np.linspace(0, 10, 20)
    ys = xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()


if __name__ == '__main__':
    #start()
    #tableLoad()
    #hist()
    plot3d()'''