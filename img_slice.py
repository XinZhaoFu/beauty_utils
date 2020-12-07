import cv2
import numpy as np
from random import randint

slice_block_size = 128
img = cv2.imread('./data/dog1.jpg')

img_row, img_col, img_channel = img.shape
resize_rate_row = int(img_row/slice_block_size)
resize_rate_col = int(img_col/slice_block_size)
resize_row = resize_rate_row * slice_block_size
resize_col = resize_rate_col * slice_block_size
img = cv2.resize(img, dsize=(resize_col, resize_row))

complement_img = np.empty(shape=(resize_row, resize_col, img_channel), dtype=np.int)
for row in range(resize_rate_row):
    for col in range(resize_rate_col):
        random_color = [randint(150, 255), randint(150, 255), randint(150, 255)]
        if randint(0, 10) < 4:
            random_color = [255*2, 255*2, 255*2]
        complement_img[row*slice_block_size:(row+1)*slice_block_size,
        col*slice_block_size:(col+1)*slice_block_size, :] = random_color[:]
        complement_img[:, col * slice_block_size:col * slice_block_size+2, :] = 255*2
    complement_img[row * slice_block_size:row * slice_block_size + 2, :, :] = 255*2

# cv2.imwrite('./data/complement_demo.jpg', complement_img)
cv2.imwrite('./data/complement_img.jpg', complement_img*0.5 + img*0.5)
