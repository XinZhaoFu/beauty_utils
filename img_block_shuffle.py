import cv2
import numpy as np
from random import randint, shuffle

slice_block_size = 256
img = cv2.imread('./data/dog1.jpg')

img_row, img_col, img_channel = img.shape
resize_rate_row = int(img_row/slice_block_size)
resize_rate_col = int(img_col/slice_block_size)
resize_row = resize_rate_row * slice_block_size
resize_col = resize_rate_col * slice_block_size
img = cv2.resize(img, dsize=(resize_col, resize_row))
num_block = resize_rate_col*resize_rate_row

block_img = np.empty(shape=(num_block, slice_block_size, slice_block_size, img_channel), dtype=np.int)
img_block_list = []
for i in range(num_block):
    img_block_list.append(i)

temp_i = 0
for row in range(resize_row):
    for col in range(resize_col):
        if row*slice_block_size>=resize_row or col*slice_block_size>=resize_col:
            continue
        block_img[temp_i, :, :, :] = img[row*slice_block_size:(row+1)*slice_block_size,
                                     col*slice_block_size:(col+1)*slice_block_size, :]
        temp_i += 1

shuffle(img_block_list)

shuffle_img = np.zeros(shape=(resize_row, resize_col, img_channel), dtype=np.int)
temp_i = 0
for row in range(resize_row):
    for col in range(resize_col):
        if row*slice_block_size>=resize_row or col*slice_block_size>=resize_col:
            continue
        shuffle_img[row*slice_block_size:(row+1)*slice_block_size,
        col*slice_block_size:(col+1)*slice_block_size, :] \
            = block_img[img_block_list[temp_i], :, :, :]
        temp_i += 1

cv2.imwrite('./data/shuffle_demo.jpg', shuffle_img)