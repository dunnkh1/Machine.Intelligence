from sklearn.datasets import load_iris
iris = load_iris()
#print(iris.keys())
#n_samples, n_features = iris.data.shape
#print (n_samples, n_features)
#print(iris.data[0])
#print((iris.data)[len(iris.data)-1])
#print(iris.target.shape)
#print(iris.data[0])
#print(iris.target[0])
#print(iris.target_names)
#print(iris.target)
import numpy as np
import matplotlib.pyplot as plt

def plot_iris_projection(x_index, y_index):
    # this formatter will label the colorbar with the correct target names
    formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

    plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
                c=iris.target)
    plt.colorbar(ticks=[0, 1, 2], format=formatter)
    plt.xlabel(iris.feature_names[x_index])
    plt.ylabel(iris.feature_names[y_index])

x_index=1
y_index=2
plot_iris_projection(x_index,y_index)