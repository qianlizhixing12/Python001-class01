from sklearn import datasets

iris = datasets.load_iris()
data, target = iris.data, iris.target
# print(data, target)
feature = iris.feature_names
# print(feature)
targetname = iris.target_names
# print(targetname)

from sklearn.model_selection import train_test_split
x_train, y_train, x_test, y_test = train_test_split(data,
                                                    target,
                                                    test_size=0.25)
print(x_train, y_train)
print(x_test, y_test)