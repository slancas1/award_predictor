#!/usr/bin/env python2.7

import got
import sys
import os
from datetime import timedelta, date


def get_hashtag(movie):
    return "#" + movie.replace(" ", "")


def date_range(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_dates(f):
    dates = list()

    start_date = get_last_date(f)
    end_date = date(2018, 3, 5)

    for single_date in date_range(start_date, end_date):
        dates.append(single_date.strftime("%Y-%m-%d"))

    return dates


def get_last_date(f):

    tweets = f.readlines()
    i = -1

    while len(tweets) + i >= 0:
        try:
            yr, mon, day = map(int, tweets[i].split('|')[0].split()[0].split('-'))
            return date(yr, mon, day)
        except:
            i -= 1

    return date(2017, 3, 1)


def write_tweets(f, query):

    dates = get_dates(f)

    for i in xrange(len(dates) - 1):

        startDate = dates[i]
        endDate = dates[i + 1]

        success = False

        while not success:
            try:
                tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(startDate).setUntil(endDate)
                tweets = got.manager.TweetManager.getTweets(tweetCriteria)

                for tweet in tweets:
                    line = "{}|{}|{}|{}\n".format(str(tweet.date), tweet.text.encode('utf-8'), str(tweet.retweets), str(tweet.favorites))
                    f.write(line)
		print "success", query, startDate, len(tweets)
		
                success = True
            except:
                continue


if __name__ == "__main__":

	movie = sys.argv[1].strip()
    
	try:
		f = open("Data/" + movie.replace(" ", "_") + ".csv", "r+")
   	except:
		os.system("touch Data/" + movie.replace(" ", "_") + ".csv")
		f = open("Data/" + movie.replace(" ", "_") + ".csv", "r+")

	hashtag = get_hashtag(movie)

    	write_tweets(f, hashtag)

    	f.close()
