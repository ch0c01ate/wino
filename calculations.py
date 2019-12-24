import math


def calculate_distance():
    pass


if __name__ == "__main__":
    a_side_of_prism = 0
    b_sides_of_prism = [i / 100 for i in range(300, 600)]
    n_air = 0
    n_optical_glass = 0
    n_wine = 0
    alpha_r = math.asin(n_wine / n_optical_glass)
    omega = math.acos(b_side_of_prism / (2 * a_side_of_prism))

    l_r = b_side_of_prism(
        math.cos(omega - alpha_r) / 2 - math.sin(omega) * math.sin(alpha_r)
    ) / (math.cos(omega - alpha_r) * math.sin(omega) * math.sin(alpha_r))
