# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread


with open('test.txt', 'w') as f:
    pass

img = imread('Private/lena.png') # 画像の読み込み
plt.imshow(img)
plt.show()