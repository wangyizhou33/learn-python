import numpy as np

# https://www.kaggle.com/code/abhayparashar31/best-numpy-functions-for-data-science-50

# 12 Min
# Return the minimum value from the array.
arr = np.array([[1, 1, 2, 3, 3], [4, 5, 6, 6, 2]])
minimum = np.min(arr, axis=1, keepdims=True)
print(minimum.shape)

# 14 unique
print(np.unique(arr, return_counts=True))

# 15 min
print(np.mean(arr, axis=1))

# 16 median
print(np.median(arr, axis=1))

# 17 digitize
a = np.array([-0.9, 0.5, 0.9, 1, 1.2, 1.4, 3.6, 4.7, 5.3])
bins = np.array([0, 1, 2, 3])
print(np.digitize(a, bins))

# 18 reshape

A = np.random.randint(15, size=(4, 3))
print(A)
print(A.reshape(3, 4))
print(A.reshape(-1))
print(A.T)

# 19 expand dim

arr = np.array([8, 14, 1, 8, 11, 4, 9, 4, 1, 13, 13, 11])
print(np.expand_dims(arr, axis=1).shape)

# 20 squeeze
arr = np.array([[8], [14], [1], [8], [11], [4], [9], [4], [1], [13], [13], [11]])
print(np.squeeze(arr).shape)

# 21 count zeros
a = np.array([0, 0, 1, 1, 1, 0])
print(np.count_nonzero(a))

# 22 argwhere
a = np.array([0, 0, 1, 1, 1, 0])
print(np.argwhere(a))

# 23 argmin argmax
arr = np.array([[0.12, 0.64, 0.19, 0.05]])
print(np.argmax(arr, axis=1))


