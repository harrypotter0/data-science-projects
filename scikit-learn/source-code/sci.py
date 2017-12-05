# import load_iris function from datasets module
from sklearn.datasets import load_iris
# save "bunch" object containing iris dataset and its attributes
iris = load_iris()
print(type(iris))
# print the iris data
print(iris.data)
# print the names of the four features
print(iris.feature_names)
# print integers representing the species of each observation
print(iris.target)
# print the encoding scheme for species: 0 = setosa, 1 = versicolor, 2 = virginica
print(iris.target_names)
# check the types of the features and response
print(type(iris.data))
print(type(iris.target))
# check the shape of the features (first dimension = number of observations, second dimensions = number of features)
print(iris.data.shape)
