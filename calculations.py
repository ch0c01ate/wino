import math


def calculate_distance():
    pass


def intersect(f1, f2):
    k1 = f1[0]
    k2 = f2[0]
    b1 = f1[1]
    b2 = f2[1]

    x = (b2 - b1)/(k1 - k2)
    y = (k1 * x + b1)

    return x, y


if __name__ == "__main__":
    a_sides_of_prism = [i / 100 for i in range(300, 600)]
    b_sides_of_prism = [i / 100 for i in range(300, 600)]
    n_air = 1
    n_optical_glass = 1.52
    n_wine =1.35407
    alpha_r = math.asin(n_wine / n_optical_glass)

    alpha_r1 = 1
    alpha_r2 = 2
    delta_k = .1

    for a_side_of_prism in a_sides_of_prism:
        for b_side_of_prism in b_sides_of_prism:
            print(f'a: {a_side_of_prism}\tb:{b_side_of_prism}')

            omega = math.acos(b_side_of_prism / (2 * a_side_of_prism))

            l_r = b_side_of_prism * (
                math.cos(omega - alpha_r) / 2 - math.sin(omega) * math.sin(alpha_r)
            ) / (math.cos(omega - alpha_r) * math.sin(omega) * math.sin(alpha_r))

            f_omega = (math.tan(omega), 0)
            f_beta_r1 = (math.tan(90 + alpha_r1), -l_r * math.tan(90 + alpha_r1))
            f_beta_r2 = (math.tan(90 + alpha_r2), (b_side_of_prism - delta_k) * math.tan(
                90 + alpha_r1))

            int1 = intersect(f_omega, f_beta_r1)
            int2 = intersect(f_omega, f_beta_r2)

            alpha1 = math.asin(math.sin(omega - alpha_r1) * n_optical_glass /
                               n_air)
            alpha2 = math.asin(math.sin(omega - alpha_r2) * n_optical_glass /
                               n_air)

            k1 = 90 + omega - alpha1
            k2 = 90 + omega - alpha2

            b1 = int1[0] * k1
            b2 = int2[0] * k2

            f_alpha1 = (k1, b1)
            f_alpha2 = (k2, b2)

            print(intersect(f_alpha1, f_alpha2))


