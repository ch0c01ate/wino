import math

def intersect(f1, f2):
    """
    Intersection of two linear functions
    :param f1: (k, b) for y = kx + b
    :param f2: (k, b) for y = kx + b
    :return: x, y -- coordinates of intersection
    """
    k1 = f1[0]
    k2 = f2[0]
    b1 = f1[1]
    b2 = f2[1]

    x = (b2 - b1) / (k1 - k2)
    y = (k1 * x + b1)

    return x, y


if __name__ == "__main__":
    # initialize list of possible prism parameters values
    a_sides_of_prism = [i / 100 for i in range(300, 600)]

    # minimum focal length of camera
    l_focal = 30

    # refractive indexes initialization
    n_air = 1
    n_optical_glass = 1.52
    n_wine1 = 1.35407 # minimum n_wine for Brix = 14
    n_wine2 = 1.38845 # maximum n_wine for Brix = 34

    # maximum and minimum internal reflection angles respectively
    alpha_r1 = math.asin(n_wine1 / n_optical_glass)
    alpha_r2 = math.asin(n_wine2 / n_optical_glass)

    # minimal distance between prism edge and point of falling of ray
    delta_k = .1

    for a_side_of_prism in a_sides_of_prism:
        print(f'a: {a_side_of_prism}\tb:{a_side_of_prism}')

        # angle of triangle in prism
        omega = math.acos(a_side_of_prism / (2 * a_side_of_prism))

        # minimum coord for ray to reflect from
        l_r = a_side_of_prism * (math.cos(omega - alpha_r1) / 2 -
                                 math.sin(omega) * math.sin(alpha_r1)) / (
                      math.cos(omega - alpha_r2) *
                      math.sin(omega) * math.sin(alpha_r2))

        # function to represent prism side
        f_omega = (math.tan(omega), 0)
        # function to represent ray1 going through prism from light source
        f_beta_r1 = (math.tan(math.pi / 2 + alpha_r1),
                     -l_r * math.tan(math.pi / 2 + alpha_r1))
        # function to represent ray1 going through prism from light source
        f_beta_r2 = (
            math.tan(math.pi / 2 + alpha_r2),
            (a_side_of_prism - delta_k) * math.tan(math.pi / 2 + alpha_r2))

        # coordinates of intersections of rays and prism side
        int1 = intersect(f_omega, f_beta_r1)
        int2 = intersect(f_omega, f_beta_r2)

        # falling angel of ray1 going from light source and prism side
        alpha1 = math.asin(
            math.sin(omega - alpha_r1) * n_optical_glass / n_air)

        # falling angel of ray1 going from light source and prism side
        alpha2 = math.asin(
            math.sin(omega - alpha_r2) * n_optical_glass / n_air)

        # coefficients for functions to represent rays going from light source
        k1 = math.tan(math.pi / 2 + omega - alpha1)
        k2 = math.tan(math.pi / 2 + omega - alpha2)
        b1 = int1[0] * k1
        b2 = int2[0] * k2

        f_alpha1 = (k1, b1)
        f_alpha2 = (k2, b2)

        # coordinates of light source in dependence from prism size
        s_coordinates = intersect(f_alpha1, f_alpha2)
        print(s_coordinates)

        # function to represent the screen
        f_screen = (0, l_focal)

        # function to represent other prism side
        k_prism1 = math.tan(math.pi - omega)
        b_prism1 = a_side_of_prism * k_prism1
        prism1 = (k_prism1, b_prism1)

        # function to represent reflected ray1
        k_reflected_ray1 = math.tan(math.pi / 2 - alpha_r1)
        b_reflected_ray1 = l_r * k_reflected_ray1
        reflected_ray1 = (k_reflected_ray1, b_reflected_ray1)

        # function to represent reflected ray2
        k_reflected_ray2 = math.tan(math.pi / 2 - alpha_r2)
        b_reflected_ray2 = (a_side_of_prism - delta_k) * k_reflected_ray1
        reflected_ray2 = (k_reflected_ray2, b_reflected_ray2)

        # coordinates of reflected rays and prism side intersections
        int_r1 = intersect(prism1, reflected_ray1)
        int_r2 = intersect(prism1, reflected_ray2)


        falling_ray1_beta = math.asin(math.sin(omega - alpha_r1) *
                                      n_optical_glass / n_wine1)
        falling_ray2_beta = math.asin(math.sin(omega - alpha_r2) *
                                      n_optical_glass / n_wine2)

        # function to represent ray1 falling on screen
        k_falling1 = math.pi - omega - falling_ray1_beta
        x = int1[0]
        y = int2[1]
        b_falling1 = y - k_falling1 * x
        falling_screen1 = (k_falling1, b_falling1)

        # function to represent ray2 falling on screen
        k_falling2 = math.pi - omega - falling_ray2_beta
        x = int1[0]
        y = int2[1]
        b_falling2 = y - k_falling2 * x
        falling_screen2 = (k_falling2, b_falling2)

        # coordinates of intersections of ray1 and ray2 falling on screen
        res_int1 = intersect(f_screen, falling_screen1)
        res_int2 = intersect(f_screen, falling_screen2)

        print(f'max difference: {res_int1[0] - res_int2[0]}m')
