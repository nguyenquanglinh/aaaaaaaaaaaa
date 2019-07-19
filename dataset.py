import pandas as pd
import matplotlib.pyplot as plt
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data'
colums=['sepal_length','sepal_With','pental_length','petal_with','class']
frame=pd.read_csv(url,names=colums)
print(frame)
iris_color={
    'Iris-setosa':'r',
    'Iris-versicolor':'b',
    'Iris-virginica':'g'
}
plt.scatter(frame['sepal_length'],frame['sepal_With'],color='r')
for i in range(len(frame['sepal_length'])):
    x=frame['pental_length'][i]
    y=frame['petal_with'][i]
    c=frame['class'][i]
    plt.scatter(y,x,color=iris_color[c])
plt.show()