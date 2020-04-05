import numpy as np


def check_board(size: int):
    """ Generate grey scale checkboard
    plt.gray()
    @param size: the size of check board
    @return:
    """
    img = np.zeros((size, size))
    for n in np.arange(0, size):
        for m in np.arange(0, size):
            if (n & 0x01) ^ (m & 0x01):
                img[n, m] = 255  # black
    # plt.matshow(img)
    return img