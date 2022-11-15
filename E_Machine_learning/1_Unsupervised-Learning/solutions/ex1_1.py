
first = pca.components_[0]
second = pca.components_[1]

print(first, second)
np.inner(first, second)

# first@second also works
# as well does pca.components_ @ pca.components_, yielding the identity matrix
