import time
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import Generator as generator
import Perceptron as perceptron


def draw_set(set_to_draw):
    class_0 = set_to_draw[set_to_draw[:, 2] == 0]
    class_1 = set_to_draw[set_to_draw[:, 2] == 1]
    plt.figure(figsize=(8, 8))
    plt.scatter(class_0[:, 0], class_0[:, 1], label='Class 0', alpha=0.5)
    plt.scatter(class_1[:, 0], class_1[:, 1], label='Class 1', alpha=0.5)


def draw_separate_curve(coef_matr, border_set):
    coef_matr = list(coef_matr) + [0] * (6 - len(coef_matr))
    k, a, b, c, d, e = coef_matr[0], coef_matr[1], coef_matr[2], coef_matr[3], coef_matr[4], coef_matr[5]

    x_min, x_max = np.min(border_set[:, 0]) - 0.3, np.max(border_set[:, 0]) + 0.3
    y_min, y_max = np.min(border_set[:, 1]) - 0.3, np.max(border_set[:, 1]) + 0.3

    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    x, y = np.meshgrid(x, y)

    z = k + a * x + b * y + c * x ** 2 + d * y ** 2 + e * x * y

    plt.contour(x, y, z, levels=[0], colors='k')
    plt.axis('equal')


def class_split(data, coefs, feature_size):
    train_set = data[:, :2]
    train_data, class_data = perceptron.prepare_data(data, feature_size)
    return np.hstack((train_set, (train_data @ coefs > 0.0).astype(int).reshape(-1, 1)))


def classification(train_set, epochs, ed_coef, K, delta, type, feature_size):
    start_time = time.time()
    W = perceptron.classification(train_set, epochs, ed_coef, K, delta, type, feature_size)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for {type}: {round(execution_time, 3)} seconds")

    set_after_class = class_split(train_set, W, feature_size)
    """ INFO: 
        confusion_matrix = {(i, j)} - i-ый класс распознан как j
    """
    cm = confusion_matrix(train_set[:, 2], set_after_class[:, 2])
    print(cm)
    accuracy = ((cm[0][0] + cm[1][1]) /
                (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1]))
    print(f"Accuracy: {accuracy}")
    draw_set(set_after_class)

    draw_separate_curve(W, set_after_class)
    plt.title(type)


def main():
    num_points = 100
    noise = 0.0
    epochs = 100
    ed_coef = 0.5

    K = 10  # K шагов градиентного спуска
    delta = 0.05  # Порог точности локального минимума

    perceptron_amount = 1
    """ INFO: 
        :returns [(x,y,c)], где x и y - координаты,  c - класс: 1 или 0
        :param
            type = "circle" для генерации кольцевой выборки
                 = "gauss" для генерации двух Гауссовых множеств
                 = "xor" для генерации двух Xor множеств
                 = "spiral" для генерации двух спиральных множеств
    """
    train_set = generator.generate(num_points, noise, "gauss")
    draw_set(train_set)

    """ INFO: 
        :param
            type = "step" для перцептрона со ступенчатой функцией активации
                 = "sigm" для перцептрона с сигмоидальной функцией активации и обратным распространением ошибки
             
            feature_size = 3 для обучения на наборах вида [1, x_1, x_2]
                         = 5 для обучения на наборах вида [1, x_1, x_2, x_1^2, x_2^2]
                         = 6 для обучения на наборах вида [1, x_1, x_2, x_1^2, x_2^2, x_1*x_2]
    """
    train_sets = np.array_split(train_set, perceptron_amount)
    for ts in train_sets:
        classification(ts, epochs, ed_coef, K, delta, "sigm", 3)

    plt.show()


main()
