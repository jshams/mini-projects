# Decision Tree
Decision trees are a classification method used in machine learning.
They are special because they are very easy to understand by people,
and people can use them to classify an item based on it's data without
having to do any complicated math.  
See these slides to get a better idea of Decision Trees: 
[Decision Tree Slides](https://jshams.github.io/mini-projects/algorithms/decision-tree/decision_tree.slides.html).

## How to use this Decision Tree
This decision tree class can create a decision tree from any kind of 
data (categorical or discreet) so long as the target values are categorical.

The `DecisionTree` class requires two parameters, `data` and `feature_names`.  
`data` - a 2d array, where each sub-array represents one row
of the data. The last column is the target or label.  
`feature_names` - an array of strings with the feature names of the data. This
is used to ask questions about specific features. The length of feature names
must match the length of a data row (the width of data).

ex:
```python
training_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 3,'Apple'],
        ['Red', 1, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon']]
feature_names = ['color', 'diameter', 'fruit']
dt = DecisionTree(training_data, feature_names)
```

### Methods of `Decision Tree`

`classify` - given a row of data, the tree will predict a value.

ex:
```python
>>> dt.classify(['Red', 1])
'Grape'
```

`__repr__` - represents the tree in string format

ex:
```python
>>> print(dt)
Is diameter >= 3?
    |--> True:
    |    Is color equal to Yellow?
    |       |--> True:
    |       |   Prediction: {'Apple': 50.0, 'Lemon': 50.0}
    |       |--> False:
    |       |   Prediction: {'Apple': 100.0}
    |--> False:
    |   Prediction: {'Grape': 100.0}
```