import numpy as np
import math


def generate(points_count, noise, type):
    if type == "circle":
        return circle_generation(points_count, noise)
    elif type == "gauss":
        return gauss_generation(points_count, noise)
    elif type == "spiral":
        return spiral_generation(points_count, noise)
    elif type == "xor":
        return xor_generation(points_count, noise)
    else:
        raise ValueError("Invalid generation type")


def circle_generation(points_count, noise):
    radius = 1.0
    inner_radius = 1.5 * radius
    outer_radius = 2.0 * radius
    first_set = generate_points_in_circle(radius, points_count, noise, 1)
    second_set = generate_points_in_ring(inner_radius, outer_radius, points_count, noise, 0)
    merged_result = np.vstack((first_set, second_set))
    np.random.shuffle(merged_result)
    return merged_result


def generate_points_in_circle(rad, points_count, noise, class_value):
    r = rad * np.sqrt(np.random.rand(points_count))
    theta = np.random.uniform(0, 2 * math.pi, points_count)
    x = r * np.cos(theta) + np.random.uniform(-noise, noise, points_count)
    y = r * np.sin(theta) + np.random.uniform(-noise, noise, points_count)
    c = np.full(points_count, class_value)
    return np.column_stack((x, y, c))


def generate_points_in_ring(in_radius, out_radius, points_count, noise, class_value):
    r = (out_radius - in_radius) * np.sqrt(np.random.rand(points_count)) + in_radius
    theta = np.random.uniform(0, 2 * math.pi, points_count)
    x = r * np.cos(theta) + np.random.uniform(-noise, noise, points_count)
    y = r * np.sin(theta) + np.random.uniform(-noise, noise, points_count)
    c = np.full(points_count, class_value)
    return np.column_stack((x, y, c))


def gauss_generation(points_count, noise):
    center_x1, center_y1 = 3, 3
    center_x2, center_y2 = -3, -3
    first_set = generate_gauss_set(center_x1, center_y1, points_count, noise, 1)
    second_set = generate_gauss_set(center_x2, center_y2, points_count, noise, 0)
    merged_result = np.vstack((first_set, second_set))
    np.random.shuffle(merged_result)
    return merged_result


def generate_gauss_set(center_x, center_y, points_count, noise, class_value):
    x = np.random.normal(center_x, 1, points_count)
    y = np.random.normal(center_y, 1, points_count)
    x += np.random.uniform(-noise, noise, points_count)
    y += np.random.uniform(-noise, noise, points_count)
    c = np.full(points_count, class_value)
    return np.column_stack((x, y, c))


def spiral_generation(points_count, noise):
    first_set = generate_spiral_set(0, points_count, noise, 1)
    second_set = generate_spiral_set(math.pi, points_count, noise, 0)
    merged_result = np.vstack((first_set, second_set))
    np.random.shuffle(merged_result)
    return merged_result


def generate_spiral_set(start_angle, points_count, noise, class_value):
    r = np.linspace(0, 5, points_count)
    theta = np.linspace(start_angle, start_angle + 1.75 * 2 * np.pi, points_count)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    x += np.random.uniform(-noise, noise, points_count)
    y += np.random.uniform(-noise, noise, points_count)
    c = np.full(points_count, class_value)
    return np.column_stack((x, y, c))


def xor_generation(points_count, noise):
    first_set = generate_xor_set(-5, -0.3, -5, -0.3, points_count // 2, noise, 1)
    second_set = generate_xor_set(0.3, 5, 0.3, 5, points_count // 2, noise, 1)
    third_set = generate_xor_set(-5, -0.3, 0.3, 5, points_count // 2, noise, 0)
    fourth_set = generate_xor_set(0.3, 5, -5, -0.3, points_count // 2, noise, 0)
    merged_result = np.vstack((first_set, second_set, third_set, fourth_set))
    np.random.shuffle(merged_result)
    return merged_result


def generate_xor_set(x_0, x_1, y_0, y_1, points_count, noise, class_value):
    x = np.random.uniform(x_0, x_1, points_count)
    y = np.random.uniform(y_0, y_1, points_count)
    x += np.random.uniform(-noise, noise, points_count)
    y += np.random.uniform(-noise, noise, points_count)
    c = np.full(points_count, class_value)
    return np.column_stack((x, y, c))
