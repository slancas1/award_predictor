#!/usr/bin.env python2.7

from datetime import datetime
import operator

# function that calculates the number of days between two certain dates
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m/%d/%Y")
    d2 = datetime.strptime(d2, "%m/%d/%Y")
    return abs((d2 - d1).days)

def get_avg(l):
    if len(l) == 0:
        return 0
    return sum(l) / float(len(l))

# function that creates a dictionary of the release dates for each movie
def release_dates():
    start_date = "02/28/2017"
    # start_date = "02/29/2016"

    rd_lines = map(str.strip, open("2017Data/reviewsAndDates.txt"))
    release_dates = dict()

    for line in rd_lines:
        movie = line.split()[0]
        date = line.split()[3]
        day = days_between(start_date, date)

        release_dates[movie] = day

    return release_dates

# function that creates the date ratio that is to be used for the classification models
def get_ratio(rd):
    c_lines = map(str.strip, open("2017Data/sentiments.csv"))
    ratios = dict()

    # 2017
    final_start = 320
    final_end = 328

    # 2016
    # final_start = 323
    # final_end = 331

    for line in c_lines:
        movie, data = line.split()
        counts = map(float, data.split(','))
        week_one = counts[rd[movie]:rd[movie] + 6]

        final_week = counts[final_start:final_end]

        #print movie, final_week

        initial_score = float(get_avg(week_one))
        final_score = float(get_avg(final_week))

        try:
            ratios[movie] = final_score / initial_score
        except:
            ratios[movie] = 0

    sorted_ratios = sorted(ratios.items(), key=operator.itemgetter(1))

    return sorted_ratios

if __name__ == "__main__":
    rd = release_dates()
    ratios = get_ratio(rd)

    for r in ratios:
        print r[0], r[1]
