from sklearn.datasets import load_iris
iris = load_iris()
#Note : print syntax was changed from `print var` in python2
#       to `print(var)` in python3.
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])
