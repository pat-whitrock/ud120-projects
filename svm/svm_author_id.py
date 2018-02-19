#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

### import the sklearn module for GaussianNB
from sklearn.svm import SVC

### create classifier
clf = SVC(kernel='rbf', C=10000)

# Reduce training set size to increase speed at the expense of accuracy
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print "precicting time:", round(time()-t0, 3), "s"

### calculate and return the accuracy on the test data
### this is slightly different than the example,
### where we just print the accuracy
### you might need to import an sklearn module
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy

# print labels for specific test features
print "preciction for element 10:", pred[10]
print "preciction for element 26:", pred[26]
print "preciction for element 50:", pred[50]

#########################################################


