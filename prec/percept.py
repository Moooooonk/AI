""" 

*기초 퍼셉트론*

def AND(x1, x2): # 입력 신호
    w1, w2, theta = 0.5, 0.5, 0.7 #가중치 및 임계값 설정
    tmp = x1*w1 + x2*w2
    
    if tmp >= theta:
        return 0
    elif tmp < theta:
        return 1
    
    print(theta)

"""
"""
배열로 퍼셉트론 간단하게 표현
import numpy as np

x = np.array([0, 1]) # 입력
w = np.array([0.5, 0.5]) # 가중치
b = -0.7 # 편향

np.sum(w*x) + b # 퍼셉트론

*배열 활용 퍼셉트론*

# 퍼셉트론의 AND, NAND, OR은 가중치와 편향의 차이. 나머지는 일치
import numpy as np

def AND(x1, x2):

    x = np.array([x1, x2]) # 입력
    w = np.array([0.5, 0.5]) # 가중치
    b = -0.7 # 편향 (연산 후 편향보다 높은 값일 때 1 반환)
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w)+b
    
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1

#다층 퍼셉트론(XOR)

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
                
"""
