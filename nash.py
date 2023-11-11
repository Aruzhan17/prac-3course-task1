import numpy as np
from typing import List
from scipy.optimize import linprog
import random
import matplotlib.pyplot as plt


def nash_equilibrium(A: np.ndarray) -> List:  #функция, которая ищет оптимальные стратегии игроков и возвращает значение игры
    matrix_negative_min = find_negative_min(A)
    p = solve(A, 'p') # Решение игры для первого игрока (вектор оптимальной стратегии)
    q = solve(A, 'q') # Решение игры для второго игрока (вектор оптимальной стратегии)
    val = 1 / np.sum(p.x)

    return (val + matrix_negative_min, p.x * val, q.x * val)


def solve(A: np.ndarray, player: str):  #ищет вектор оптимальной стратегии игрока
    if player == 'p':
        c = np.ones(A.shape[0]) # заполняет вектор единицами (размер кол-во строк)
        b = -np.ones(A.shape[1]) # заполняет вектор -1 (размер кол-во столбцов)
        return linprog(c, A_ub=np.transpose(np.negative(make_positive(A))), b_ub=b) # симпликс метод (ищет вектор оптимальных стратегий)
    elif player == 'q':
        b = np.ones(A.shape[0])
        c = -np.ones(A.shape[1])
        return linprog(c, A_ub=make_positive(A), b_ub=b)
    else:
        raise ValueError('Invalid player: ' + player)


def print_solution(v: List):
    val, solution1, solution2 = v[0], v[1], v[2]

    print(f"Value: {val}")
    print(f"p: {solution1}")
    print(f"q: {solution2}")
    visualize_strategies(solution1, solution2, val)


def visualize_strategies(solution1: np.array, solution2: np.array, val: float):  #визуализация графика
    fig, axs = plt.subplots(figsize=(10, 5), ncols=2)  #строим два точечных графика
    
    axs[0].scatter(range(1, len(solution1)+1), solution1, color='b', s=50, alpha=1) #х: кол-во столбцов, у:значение вектора
    axs[0].set_title('First player optimal strategy')
    axs[0].set_xlim(0, None)
    axs[0].set_ylim(0, None)
    axs[0].grid(axis='x', linestyle='dotted', linewidth=.5)

    axs[1].scatter(range(1, len(solution2)+1), solution2, color='r', s=50, alpha=1)
    axs[1].set_title('Second player optimal strategy')
    axs[1].set_xlim(0, None)
    axs[1].set_ylim(0, None)
    axs[1].grid(axis='x', linestyle='dotted', linewidth=.5)
    
    plt.show()


def make_positive(A: np.ndarray):  # к каждому элементу добавляет мин значение, получится один 0 и тд
    A += -find_negative_min(A)
    return A


def find_negative_min(A: np.ndarray):
    min_val = np.amin(A)
    if min_val <= 0:
        return min_val - 1
    else:
        return 0


def random_matrix(h: int, w: int):
    A = np.ones((h, w), dtype=int)
    for i in range(h):
        for j in range(w):
            A[i, j] = random.randint(-10, 10)
    print()
    for i in range(h):
        for j in range(w):
            print(A[i, j], ' ', end='')
        print()
    return A
