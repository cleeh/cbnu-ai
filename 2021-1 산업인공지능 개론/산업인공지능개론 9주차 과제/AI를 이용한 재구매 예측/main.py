if __name__ == '__main__':
	MEMBER_NO = 0
	MEMBER_SEX = 1
	MEMBER_BIRTH = 2
	MEMBER_CONNECTION_COUNT = 3
	ORDER_NO = 4
	ORDER_STATUS = 5
	PRODUCT_NO = 6
	ORDER_PRODUCT_QUANTITY = 7
	ORDER_PRODUCT_PRICE = 8
	ORDER_DATE = 9

	f = open('order.csv', 'r', encoding='euc-kr')
	reader = csv.reader((line.replace('\0','') for line in f))
	header = next(reader)

# 	with open('features.data', 'rb') as file:
# 	   pickle_features = pickle.load(file)
# 	   pickle_cycles = pickle.load(file)
# 	   print(pickle_features)
# 	   print(pickle_cycles)

	order_list = OrderList()
	members_no = set()
	products_no = set()
	for row in tqdm(reader):	
	    order = Order(
	        row[MEMBER_NO],
	        row[MEMBER_CONNECTION_COUNT],
	        row[PRODUCT_NO],
	        row[ORDER_PRODUCT_PRICE],
	        row[ORDER_PRODUCT_QUANTITY],
	        row[ORDER_DATE]
	    )
	    order_list.add(order)
	f.close()

	with open('features.data', 'wb') as file:
	    pickle.dump(np.array([feature.as_list() for feature in features]), file)
	    pickle.dump(np.array(cycles), file)

	import tensorflow as tf
	from keras.models import Sequential
	from keras.layers import Dense, Dropout
	from keras.optimizers import adam

	x_train, y_train = np.array([feature.as_list() for feature in features[:30000]]), np.array(cycles[:30000])
	x_test, y_test = np.array([feature.as_list() for feature in features[30000:40000]]), np.array(cycles[30000:40000])
	x_val, y_val = np.array([feature.as_list() for feature in features[40000:]]), np.array(cycles[40000:])

	training_epochs = 15
	batch_size = 1

	# 2. 모델 구성
	model = Sequential([
	    Dense(8, activation='relu'),
	    Dropout(0.3),
	    Dense(1000, activation='sigmoid'),
	    Dropout(0.3),
	    Dense(1000, activation='relu'),
	    Dropout(0.3),
	    Dense(1, activation='relu'),
	])
	model.compile(
	    loss='mse',
	    optimizer='adam',
	    metrics=[tf.keras.metrics.MeanSquaredError()])

	# 3. 훈련
	model.fit(
	    x_train,
	    y_train,
	    epochs=training_epochs,
	    batch_size=batch_size,
	    validation_data=(x_val, y_val))

	# 4. 평가 예측
	evaluation = model.evaluate(x_test, y_test, batch_size=batch_size)
	print('MSE: {}'.format(evaluation[1]))

	# 5. 시각화
	import matplotlib.pyplot as plt
	plt.ylim(0, 200)
	plt.plot(y_test[250:400])
	plt.plot(y_predict[250:400])
	plt.show()
	