from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
mnist = fetch_openml('mnist_784')
print('Dataset: {}'.format(mnist.keys()))
print('Image Shape: {}'.format(mnist['data'].shape))
mnist.data = mnist.data / 255.0
x_train = mnist.data[:60000]
x_test = mnist.data[60000:]
y_train = np.int16(mnist.target[:60000])
y_test = np.int16(mnist.target[60000:])

# MLP 분류기 모델을 학습
mlp = MLPClassifier(
    hidden_layer_sizes=(100), # 은닉층 100개
    learning_rate_init=0.001, # 학습률
    batch_size = 512, # 배치 크기
    max_iter = 300, # 최대 반복수
    solver = 'adam', # Adam Optimizer - https://seamless.tistory.com/38
    verbose = True) # 학습 출력 활성화
mlp.fit(x_train, y_train)

# 테스트 집합으로 예측
res = mlp.predict(x_test)

# 혼동 행렬
conf = np.zeros((10, 10), dtype = np.int16)
for i in range(len(res)):
  conf[res[i]][y_test[i]] += 1
print(conf)

# 정확률 계산
no_correct = 0
for i in range(10):
  no_correct += conf[i][i]
accuracy = no_correct/len(res)
print('테스트 집합에 대한 정확률은 {}%입니다.'.format(accuracy * 100))
