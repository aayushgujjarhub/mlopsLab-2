from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [100, 200, 300, 400, 500]

model = LinearRegression()
model.fit(X, y)

print("Predicted price:", model.predict([[6]])[0])