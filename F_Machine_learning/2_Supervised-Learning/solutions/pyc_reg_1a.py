
X, y = make_regression(n_samples=200, n_features=1, 
                             n_informative=1, noise=30, random_state=42)

sns.scatterplot(X.flatten(), y.flatten())
