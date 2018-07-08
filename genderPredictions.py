
from sklearn import tree

#clf(short for classifier) is a variable tthat stores the decision tree model
#clf will store the decision tree classifier
#The tree dependency can be referenced directly by calling it here
#The decision tree is then initialised by calling the decision tree method on the tree object
clf = tree.DecisionTreeClassifier()

#Will later add more classifiers




# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Train more classifiers here

#The fit method trains the decision tree on the provided data set
clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

# Eventually compare their reusults and print the best one!

print(prediction)