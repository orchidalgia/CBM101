
df = pd.DataFrame({'X1': [i[0] for i in X],
                   'X2': [i[1] for i in X],
                   'y': y.flatten()})

# another way
df = pd.DataFrame({'X1': X[:, 0],
                   'X2': X[:, 1],
                   'y': y.flatten()})
