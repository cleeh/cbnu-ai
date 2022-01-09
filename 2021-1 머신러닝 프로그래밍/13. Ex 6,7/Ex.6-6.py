import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# CIFAR-10 데이터셋을 읽고 신경망에 입력할 형태로 변환
(x_train, y_train), (x_test, y_test) = cifar10.load_data() # 32 * 32 이미지 모음
x_train = x_train.astype(np.float32) / 255.0 # (256, 256, 256) -> (1, 1, 1) normalize
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10) # 다차원 -> 1차원 3 * 3 * 3 => 27개
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 신경망 모델 설계
# TODO: Dropout 수치 변경, activiation 함수 변경 => 영향이 어떻게 되는가
cnn = Sequential()
cnn.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
cnn.add(Conv2D(32, (3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2))) # 2 * 2 -> max()
cnn.add(Dropout(0.25))
cnn.add(Conv2D(64, (3, 3), activation='relu'))
cnn.add(Conv2D(64, (3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Dropout(0.25))
cnn.add(Flatten()) # 1차원 변경
cnn.add(Dense(512, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(10, activation='softmax'))

# 신경망 모델 학습
cnn.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
hist = cnn.fit(x_train, y_train, batch_size=128, epochs=30, validation_data=(x_test, y_test), verbose=2)

# 모델의 정보 출력
cnn.summary()

# 컨볼루션층 커널 시각화
for layer in cnn.layers:
    if 'conv' in layer.name:
        kernel, biases = layer.get_weights()
        print(layer.name, kernel.shape)

kernel, biases = cnn.layers[0].get_weights() # 층 0의 커널 정보 저장
minv, maxv = kernel.min(), kernel.max()
kernel = (kernel - minv) / (maxv - minv)
n_kernel = 32

plt.figure(figsize=(20, 3))
plt.suptitle("Kernels of conv2d_4")
for i in range(n_kernel):
    f = kernel[:, :, :, i]
    for j in range(3):
        plt.subplot(3, n_kernel, j*n_kernel + i + 1)
        plt.imshow(f[:, :, j], cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.title('{}_{}'.format(i, j))
plt.show()

# 컨볼루션층 특징 맵 시각화
for layer in cnn.layers:
    if 'conv' in layer.name:
        print(layer.name, layer.output.shape)
        
partial_model = Model(inputs=cnn.inputs, outputs=cnn.layers[0].output) # 층 0만 떼어냄
partial_model.summary()

feature_map = partial_model.predict(x_test) # 부분 모델로 테스트 집합을 예측
fm = feature_map[1] # 1번 영상의 특징 맵을 시각화

plt.imshow(x_test[1]) # 1번 영상을 출력

plt.figure(figsize=(20, 3))
plt.suptitle("Feature maps of conv2d_4")
for i in range(32):
    plt.subplot(2, 16, i + 1)
    plt.imshow(fm[:, :, i], cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.title("map{}".format(i))
plt.show()