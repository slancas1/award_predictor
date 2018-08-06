#!/usr/bin/env python2.7

# this file combines the tweet count and tweet sentiment into a single file
import os

files = dict()

for metric in ["Counts", "Sentiments"]:

    filename = metric.lower() + ".csv"

    os.system('touch {}'.format(filename))
    files[metric] = open(filename, "w")

    for f in os.listdir(metric):
        movie = f.strip().replace(".csv", "").replace("_", "-")
        for line in open(metric + "/" + f):
            files[metric].write("{} {}\n".format(movie, line.strip()))
            break

    files[metric].close()
