from sklearn.linear_model import LinearRegression

# sample training data
months = [[1],[2],[3],[4]]
costs = [120,130,145,160]

model = LinearRegression()
model.fit(months,costs)

prediction = model.predict([[5]])

print("Predicted next month cost:", prediction[0])
