import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
#그래프 표현

x = np.arange(0, 6, 0.1) # 0부터 6까지 0.1 간격으로 np 배열 생성
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="sin", linestyle = "--")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin, cos')
plt.legend
plt.show 


#이미지 표현

img = imread('이미지이름.png') #경로설정 확인

plt.imshow(img)
plt.show()

