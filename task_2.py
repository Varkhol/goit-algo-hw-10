import random
import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

a = 0
b = 2

def monte_carlo_integral(f, a, b, num_points=100_000):
    x_samples = [random.uniform(a, b) for _ in range(1000)]
    y_max = max(f(x) for x in x_samples)

    points = [(random.uniform(a, b), random.uniform(0, y_max)) for _ in range(num_points)]

    inside_points = [point for point in points if point[1] <= f(point[0])]

    M = len(inside_points)
    N = len(points)
    rectangle_area = (b - a) * y_max
    integral = (M / N) * rectangle_area

    return integral

def monte_carlo_simulation(f, a, b, num_experiments=100, num_points=15_000):
    average_area = 0

    for _ in range(num_experiments):
        area = monte_carlo_integral(f, a, b, num_points)
        average_area += area

    average_area /= num_experiments
    return average_area


def draw_plot(f, a, b):

    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def main():
    draw_plot(f, a, b)

    # 1. Метод Монте-Карло (один експеримент, багато точок)
    mc_result = monte_carlo_integral(f, a, b, num_points=100_000)

    # 2. Метод Монте-Карло (серія експериментів)
    mc_avg_result = monte_carlo_simulation(f, a, b, num_experiments=100, num_points=15_000)

    # 3. Аналітичний розрахунок:
    analytical_result = 8 / 3

    # 4. Перевірка через scipy.integrate.quad
    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Функція: f(x) = x²")
    print(f"Межі інтегрування: [{a}, {b}]\n")
    print(f"Монте-Карло (100 000 точок):             {mc_result:.6f}")
    print(f"Монте-Карло (100 експериментів):         {mc_avg_result:.6f}")
    print(f"Аналітичний результат (x³/3):            {analytical_result:.6f}")
    print(f"quad (scipy):                            {quad_result:.6f} (похибка: {quad_error:.2e})")


if __name__ == "__main__":
    main()