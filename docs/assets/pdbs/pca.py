##Statistics Libraries
import numpy as np
import sklearn
from sklearn.decomposition import PCA
##Plotting Library
import matplotlib.pyplot as plt


# #############################################################################
# Create the data

X = np.array([[-1, -1],
              [-2, -1],
              [-3, -2],
              [1, 1],
              [2, 1]])

mu = X.mean(axis=0)




# #############################################################################
# Perform PCA

pca = PCA(n_components=2)

pca.fit(X)

print('PCA eigenvectors')
print(pca.components_)
print('PCA Variance')
print(pca.explained_variance_ratio_)
eigenvectors=pca.components_
projected_data = np.dot(X, eigenvectors)
sigma = projected_data.std(axis=0).mean()


# #############################################################################
# Plotting


fig, ax = plt.subplots()
ax.scatter(X[:,0],X[:,1])
for axis in eigenvectors:
    start, end = mu, mu + sigma * axis
    ax.annotate(
        '', xy=end, xycoords='data',
        xytext=start, textcoords='data',
        arrowprops=dict(facecolor='red', width=2.0))

ax.set_aspect('equal')
plt.show()


plt.xlabel('PCA #')
plt.ylabel('Variance')
plt.title('PCA Analysis')
plt.plot(pca.explained_variance_ratio_)
plt.show()
