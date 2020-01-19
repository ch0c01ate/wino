from PIL import Image
import numpy


if __name__ == '__main__':
    IMG = Image.open('tmp/ex.jpg')
    NP_ARR = numpy.array(IMG)
