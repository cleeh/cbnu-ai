from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# 데이터 셋을 훈련 집합(60%)과 테스트 집합(40%)으로 분할
digit = datasets.load_digits()
print('Dataset: {}'.format(digit.keys()))
print('Image Shape: {}'.format(digit.images.shape))
x_train, x_test, y_train, y_test = train_test_split(
    digit.data,
    digit.target,
    train_size=0.6)

# MLP 분류기 모델을 학습
mlp = MLPClassifier( # https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    hidden_layer_sizes=(100), # 은닉층 100개
    learning_rate_init = 0.001, # 학습률
    batch_size = 32, # 입력 Batch
    max_iter = 300, # 최대 반복 횟수
    solver = 'sgd', # Stochastic Gradient Descent.
    verbose=True) # 학습 진행 출력
mlp.fit(x_train, y_train) # 학습

# 테스트 집합으로 예측
res = mlp.predict(x_test) # 예측

# 혼동 행렬 - https://truman.tistory.com/179
conf = np.zeros((10, 10))
for i in range(len(res)):
  conf[res[i]][y_test[i]] += 1
print(conf)

# 정확률 계산
no_correct = 0
for i in range(10):
  no_correct += conf[i][i]
  accuracy = no_correct / len(res)
print('테스트 집합에 대한 정확률은 {}% 입니다.'.format(accuracy * 100))