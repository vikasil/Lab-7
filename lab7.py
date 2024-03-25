import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter


def task1():
    arr = [randint(0,100) for _ in range(10**6)]
    arr2 = [randint(0,100) for _ in range(10**6)]
    time.start = time.perf_counter()
    result = [arr[i] * arr2[i] for i in range(10**6)]
    time.end = time.perf_counter()
    print("время выполнения операции поэлементного перемножения стандартных списков", time.end-time.start)
    time.start = time.perf_counter()
    result = np.multiply(np.array(arr),np.array(arr2))
    time.end = time.perf_counter()
    print("время выполнения операции поэлементного перемножения массивов NumPy", time.end-time.start)



def task2():
    arr = pd.read_csv("data2.csv")
    plt.figure(1)
    plt.hist(arr["Solids"], bins=20)
    plt.title("histogram")
    plt.xlabel("Solids")
    plt.ylabel("quantity")
    #plt.show()

    plt.figure(2)
    plt.hist(arr["Solids"], bins=20, color="green", density=True)
    plt.title("histogram2")
    plt.xlabel("Solids")
    plt.ylabel("quantity")
    #plt.show()

    print(round(arr["Solids"].std(), 2), "среднеквадратичное отклонение")


def task3():
    x = np.linspace(-np.pi, np.pi)
    y = 1/x
    z = np.sin(x)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z, label="parametric curve")
   # plt.show()


def additional_task():
    def update(frame):
        line.set_ydata(np.sin(x + frame / 8))
        return line,
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.01)
    line, = ax.plot(x, np.sin(x))
    ani = FuncAnimation(fig, update, frames=150, blit=True)
    writer = PillowWriter(fps=50)
    plt.show()
    ani.save("y=sin(x).gif", writer=writer)

if __name__ == "__main__":
    task1()
    task2()
    task3()
    print("Пожалуйста, не закрывайте программу!")
    print("Идёт запись гифки!")
    additional_task()
    print("Гифка сохранена")
