import numpy as np
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import font_manager
import matplotlib.pyplot as plt

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

plt.rc('font', family='Malgun Gothic')

## 데이터 읽어오기
health_df = pd.read_csv('./data/국민건강보험공단_건강검진정보_20191231.csv', encoding='euc-kr')

## 데이터 확인
health_df.info()
print(health_df.describe())

## 데이터 왜곡 (공란 데이터 채우기)
print(health_df.isnull().sum())
for feature in ('허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)',
                '수축기 혈압', '이완기 혈압', '식전혈당(공복혈당)', '총 콜레스테롤', '트리글리세라이드',
                'HDL 콜레스테롤', 'LDL 콜레스테롤', '혈색소', '요단백', '혈청크레아티닌',
                '(혈청지오티)AST', '(혈청지오티)ALT', '감마 지티피'):
  health_df[feature].fillna(health_df[feature].dropna().median(), inplace=True)

# 1 값이 가장 많음
# health_df['흡연상태'].plot(kind='hist', title='흡연상태 그래프 (1 값이 가장 많음)')
# plt.show()
health_df['흡연상태'].fillna(1, inplace=True)

# Nan 값이 0을 대체할 필요가 있음
# health_df['음주여부'].plot(kind='hist', title='음주여부 그래프 (Nan 값을 0으로 대체할 필요가 있음)')
# plt.show()
health_df['음주여부'].fillna(0, inplace=True)

print(health_df.isnull().sum())

# 불필요 데이터 삭제
health_df = health_df.drop('기준년도', axis=1)
health_df = health_df.drop('데이터 공개일자', axis=1)

# 유일 데이터 삭제
health_df = health_df.drop('가입자 일련번호', axis=1)

# 미시행 검사 데이터 삭제
health_df = health_df.drop('결손치 유무', axis=1)
health_df = health_df.drop('치아마모증유무', axis=1)
health_df = health_df.drop('제3대구치(사랑니) 이상', axis=1)

health_df.info()

# Nan 데이터 삭제
cropped_health_df = health_df.dropna(axis=0)

## 데이터간 상관관계 분석 (Pearson Correlation)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(health_df.corr())

xaxis = np.arange(health_df.shape[1])
ax.set_xticks(xaxis)
ax.set_yticks(xaxis)
ax.set_xticklabels(health_df.columns.values)
ax.set_yticklabels(health_df.columns.values)
plt.setp(ax.get_xticklabels(), rotation=60, ha="left", va="center", rotation_mode="anchor")

plt.title('데이터간 상관관계', y=-1)
plt.show()


cropped_health_df = health_df.dropna(axis=0)

## 데이터 분할
target_feature = '성별코드'
train_df, test_df = np.split(cropped_health_df, [int(.7*len(cropped_health_df))])

X_train = train_df.drop(target_feature, axis=1)
Y_train = train_df[target_feature]
X_test  = test_df.drop(target_feature, axis=1).copy()
print('훈련 데이터, 훈련 라벨, 테스트 데이터 크기:', X_train.shape, Y_train.shape, X_test.shape)

## Model 생성 및 Prediction
# Perceptron
perceptron = Perceptron()
perceptron.fit(X_train, Y_train)
Y_pred = perceptron.predict(X_test)
acc_perceptron = round(perceptron.score(X_train, Y_train) * 100, 2)
print('Perceptron', acc_perceptron)

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)
acc_log = round(logreg.score(X_train, Y_train) * 100, 2)
print('Logistic Regression', acc_log)

# Decision Tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)
Y_pred = decision_tree.predict(X_test)
acc_decision_tree = round(decision_tree.score(X_train, Y_train) * 100, 2)
print('Decision Tree', acc_decision_tree)

# Gaussian Naive Bayes
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict(X_test)
acc_gaussian = round(gaussian.score(X_train, Y_train) * 100, 2)
print('Gaussian Naive Bayes', acc_gaussian)

# Stochastic Gradient Descent
sgd = SGDClassifier()
sgd.fit(X_train, Y_train)
Y_pred = sgd.predict(X_test)
acc_sgd = round(sgd.score(X_train, Y_train) * 100, 2)
print('Stochastic Gradient Descent', acc_sgd)

# Linear SVC
linear_svc = LinearSVC()
linear_svc.fit(X_train, Y_train)
Y_pred = linear_svc.predict(X_test)
acc_linear_svc = round(linear_svc.score(X_train, Y_train) * 100, 2)
print('Linear SVC', acc_linear_svc)

# Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
random_forest.score(X_train, Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)
print('Random Forest', acc_random_forest)

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print('KNN Classifier', acc_knn)

# Support Vector Machines
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print('Support Vector Machines', acc_svc)

models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', 
              'Random Forest', 'Naive Bayes', 'Perceptron', 
              'Stochastic Gradient Decent', 'Linear SVC', 
              'Decision Tree'],
    'Score': [acc_svc, acc_knn, acc_log, 
              acc_random_forest, acc_gaussian, acc_perceptron, 
              acc_sgd, acc_linear_svc, acc_decision_tree]})
print(models.sort_values(by='Score', ascending=False))