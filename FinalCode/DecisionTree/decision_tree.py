#!/usr/bin/env python2.7

#from scipy import stats
#import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from collections import defaultdict
#from sklearn.metrics import mean_squared_error

award_count = defaultdict(int)


def train(data, awards):

    X, Y, _ = get_dataset(data, awards)

    clf = RandomForestClassifier(n_estimators=1000)
    #clf = DecisionTreeClassifier()
    #clf = MLPClassifier(max_iter=1000)

    clf.fit(X, Y)

    #tree.export_graphviz(clf, out_file='tree.dot', class_names=True, filled=True, impurity=True)

    return clf


def test(clf, data, awards):
    X, true_Y, movies = get_dataset(data, awards)

    predict_Y = clf.predict(X)

    #print predict_Y

    error = get_error(true_Y, predict_Y, movies)

    #return mean_squared_error(test_Y, predicting_Y)


def get_error(true_Y, predict_Y, movies):

    print_Y(true_Y, predict_Y, movies)


def print_Y(true_Y, predict_Y, movies):

    correct = 0
    wrong = 0

    for i in range(len(true_Y)):

        if predict_Y[i] == 1:
            award_count[movies[i]] += 1


def get_dataset(data, awards):

    X = list()
    Y = list()
    movies = list()

    for line in data:

        movie = line.split(",")[0]
        movies.append(movie)

        fields = map(float, line.split(",")[1:])

        if awards:
            x = fields[:-3] + fields[-2:]
            y = int(fields[-3])
        else:
            x = fields[:-1]
            y = int(fields[-1])

        X.append(x)
        Y.append(y)

    return X, Y, movies


def run_dt():

    awards = True

    file1 = "final_awards_2016.csv" if awards else "final_no_awards_2016.csv"
    file2 = "final_awards_2017.csv" if awards else "final_no_awards_2017.csv"

    training_data = map(str.strip, open(file1).readlines())
    testing_data = map(str.strip, open(file2).readlines())

    for _ in range(100):

        clf = train(training_data, awards)
        test(clf, testing_data, awards)


    for k in award_count:
        print k, award_count[k]



if __name__ == "__main__":
    run_dt()
