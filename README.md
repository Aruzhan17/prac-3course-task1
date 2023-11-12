[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/products/distribution)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](http://www.numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](http://matplotlib.org/)


# Практикум 3 курс. Осень 2023 - Весна 2024


## Цель курса
Основной целью данного курса является знакомство с современными практиками и инструментами разработки ПО, включая:
- работу с системой контроля версий,
- совместную работу над задачами при помощи Github,
- работу с динамическим типизированным языком программирования (Python)
- использование Jupyter для быстрого прототипирования и визуализации полученных результатов,
- автоматизированное тестирование кода,
- etc.

### Необходимые библиотеки
Для того, чтобы начать выполнять задания достаточно установить:
* numpy
* scipy
* matplotlib

### Описание
* ```nash.py``` --- содержит реализацию функции ```nash_equilibrium(A: np.ndarray)``` и некоторых вспомогательных функций
* ```nash.ipynb``` --- Jupyter notebook с визуализацией векторов оптимальных стратегий для различных примеров
* ```run.py``` --- юнит-тесты
	* Для запуска юнит-тестов необходимо выполнить: ```python3 run.py```

### Contributors
* Искакова Аружан
	* Реализация функции поиска векторов оптимальной стратегии игроков ```nash_equilibrium(A: np.ndarray)```
	* Реализация функции визуализации векторов оптимальных стратегий с помощью matplotlib
	* Реализация юнит-тестов
* Мухамеджанова Томирис
	* Визуализация примеров поиска оптимальных стратегий в случае полного и не полного спектра оптимальной стратегии, спектра, состоящего из одной точки
	* Визуализация случая рандомной матрицы выигрыша для поиска оптимальных стратегий
