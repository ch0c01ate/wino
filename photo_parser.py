from PIL import Image
import numpy
import math


def to_dict(img):
    res = dict()
    for row in range(len(img)):
        for col in range(len(img)[row]):
            val = img[row][col]
            if val not in res:
                res[val] = (row, col)


def get_med(img):
    tmp = sorted(img.keys())
    return tmp[len(tmp) // 2]


def get_med_coords(img, med, accuracy=10):
    pass


if __name__ == '__main__':
    IMG = Image.open('tmp/ex.jpg')
    NP_ARR = numpy.array(IMG)
