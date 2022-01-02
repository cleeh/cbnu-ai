# 산업인공지능개론 13주차 과제

## 입력 사진의 일부

![입력사진](https://github.com/rockatoo/cbnu-ai/blob/master/2021-1%20%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EA%B0%9C%EB%A1%A0/%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B0%9C%EB%A1%A0%2013%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C/1.%20%EC%9E%85%EB%A0%A5%20%EC%82%AC%EC%A7%84%EC%9D%98%20%EC%9D%BC%EB%B6%80.png "입력 사진의 일부")"

## Resnet 모델 예측
Resnet 모델에 포장용기 이미지 학습 후 예측

![Resnet 모델 예측](https://github.com/rockatoo/cbnu-ai/blob/master/2021-1%20%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EA%B0%9C%EB%A1%A0/%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B0%9C%EB%A1%A0%2013%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C/2.%20ResNet%20%EB%AA%A8%EB%8D%B8%20%EC%98%88%EC%B8%A1.png "Resnet 모델 예측")

## 전이학습 모델 예측
Resnet 모델의 마지막 층을 제외한 층들을 다른 사람들이 학습해 얻은 수치를 가져온다.
그 후 Resnet 모델의 마지막 층을 정하기 위해 포장용기 이미지 학습 후 예측

![전이학습한 Resnet 모델 예측](https://github.com/rockatoo/cbnu-ai/blob/master/2021-1%20%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EA%B0%9C%EB%A1%A0/%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B0%9C%EB%A1%A0%2013%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C/3.%20%EC%A0%84%EC%9D%B4%ED%95%99%EC%8A%B5%20%EB%AA%A8%EB%8D%B8%20%EC%98%88%EC%B8%A1.png "전이학습한 Resnet 모델 예측")

## 모델 간 정확도/손실 비교

### Resnet 모델 정확도/손실
Resnet의 모든 층을 학습한 결과

![Resnet 모델 정확도/손실](https://github.com/rockatoo/cbnu-ai/blob/master/2021-1%20%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EA%B0%9C%EB%A1%A0/%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B0%9C%EB%A1%A0%2013%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C/resnet.png "Resnet 모델의 정확도/손실")

### 전이학습 모델 정확도/손실
포장용기가 아닌 다른 이미지를 이용해 학습한 Resnet 모델을 사용했음에도 준수한 성능을 보인다.

![전이학습 모델 정확도/손실](https://github.com/rockatoo/cbnu-ai/blob/master/2021-1%20%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EA%B0%9C%EB%A1%A0/%EC%82%B0%EC%97%85%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B0%9C%EB%A1%A0%2013%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C/transfer_learning%20resnet.png "전이학습 모델의 정확도/손실")

### 결론
전이학습한 모델보다 모델의 입력에 사용할 이미지들로 직접 학습한 모델이 정확도가 더 높다.
이번 과제에서 사용한 모델은 작기때문에 학습 시간에 큰 차이가 없지만, 모델이 커질경우 학습 시간이 매우 길어질 것이다.
따라서 학습시간을 아끼기 위해 전이학습을 활용하는 것은 도움이 될 것이다.
