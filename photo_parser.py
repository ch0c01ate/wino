from PIL import Image
import numpy


def to_dict(img):
    res = dict()
    for row in range(len(img)):
        for col in range(len(img[row])):
            val = tuple(img[row][col])
            if val not in res:
                res[val] = [(row, col)]
            else:
                res[val].append((row, col))
    return res


def get_med_color(img):
    tmp = sorted(img.keys())
    return tmp[len(tmp) // 2]


def get_col_coords(color, img):
    row = len(img) // 2
    min_tmp = float('inf')
    res = 0, 0
    for column in range(len(img[row])):
        col = img[row][column]
        diff = 0
        for i in range(len(col)):
            diff += abs(color[i] - col[i])
            if diff < min_tmp:
                min_tmp = diff
                res = row, column
    return res


if __name__ == '__main__':
    IMG = Image.open('tmp/ex.jpg')
    NP_ARR = numpy.array(IMG)
    # print(list(NP_ARR))
    med_col = get_med_color(to_dict(NP_ARR))
    print(med_col)
    print(get_col_coords(med_col, NP_ARR))
    print(len(NP_ARR[0]))
