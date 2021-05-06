import cv2
import numpy as np
from random import randint


def exchange_block(img, ex1_pos=(0, 0), ex2_pos=(0, 0), size=100):
    ex_img = np.empty(shape=img.shape, dtype=np.uint8)
    ex_img[:, :, :] = img[:, :, :]
    ex_img[ex1_pos[0]:ex1_pos[0]+size, ex1_pos[1]:ex1_pos[1]+size, :] =\
        img[ex2_pos[0]:ex2_pos[0]+size, ex2_pos[1]:ex2_pos[1]+size, :]
    ex_img[ex2_pos[0]:ex2_pos[0]+size, ex2_pos[1]:ex2_pos[1]+size, :] =\
        img[ex1_pos[0]:ex1_pos[0]+size, ex1_pos[1]:ex1_pos[1]+size, :]

    return ex_img


s_size = 300
img = cv2.imread('./data/test.jpg')

img_row, img_col, img_channel = img.shape
resize_rate_row = int(img_row / s_size)
resize_rate_col = int(img_col / s_size)
resize_row = resize_rate_row * s_size
resize_col = resize_rate_col * s_size
print(resize_col, resize_row)
img = cv2.resize(img, dsize=(resize_col, resize_row))

complement_img = np.empty(shape=(resize_row, resize_col, img_channel), dtype=np.uint8)
for row in range(resize_rate_row):
    for col in range(resize_rate_col):
        random_color = [randint(150, 255), randint(150, 255), randint(150, 255)]
        complement_img[row * s_size:(row + 1) * s_size, col * s_size:(col + 1) * s_size, :] = random_color[:]
        complement_img[:, col * s_size:col * s_size + 2, :] = 255
    complement_img[row * s_size:row * s_size + 2, :, :] = 255


ex1_pos_list, ex2_pos_list = [(0, 0), (1200, 0), (1800, 600), (300, 1500)], [(900, 1800), (0, 1200), (1500, 1800), (300, 0)]
for index in range(4):
    img = exchange_block(img, ex1_pos_list[index], ex2_pos_list[index], size=300)


cv2.imwrite('./data/complement_img.jpg', complement_img * 0.5 + img * 0.5)



