import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.target, test_idx, axis=0) #wtf is this axis shit?

#testing data
test_target = iris.target[test_idx] #variable for training
test_data = iris.data[test_idx]     #    "    for testing

#create a classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)