
test_score = knn.score(X_test, y_test)
train_score = knn.score(X_train, y_train)
print(f"test score: {test_score} \ntrain score: {train_score}")

# Notice that the train score is higher. 
# This is because the test set is unseen until now, 
# and thus more "difficult" to get right.
# if train score is much higher it might tell you about overfitting
