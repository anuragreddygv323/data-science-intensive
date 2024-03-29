#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
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

features_train = features_train[:len(features_train)] 
labels_train = labels_train[:len(labels_train)] 

from sklearn.svm import SVC

clf = SVC(C=10000,kernel='rbf')
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred=clf.predict(features_test)
print("predicting time:", round(time()-t1, 3), "s")
print('The accuracy of this classifier is: ',clf.score(features_test,labels_test))

print(pred[10])
print(pred[26])
print(pred[50])

print(list(pred).count(1))


#########################################################


