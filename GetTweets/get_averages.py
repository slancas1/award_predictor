import os
from textblob import TextBlob
from datetime import timedelta, date
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Movie:
    def __init__(self, dates, counts, sentiments):
        self.dates = dates
        self.counts = counts
        self.sentiments = sentiments
        self.lines = set()

	# function that gets the date and the text in the tweet  
    def add_tweet(self, line):
        try:
            line = line.encode(encoding='UTF-8')
            if line not in self.lines:
                timestamp, text = map(str.strip, line.split('|')[:2])
                date = timestamp.split()[0].strip()
                if date in dates:
                    self.dates[date].append(text)
                    self.lines.add(line)
        except:
            return

	# function that gets the twitter counts
    def get_counts(self):
        for d in self.dates:
            self.counts[d] = len(self.dates[d])

        return [self.counts[k] for k in sorted(self.counts)]

	# function that gets the twitter sentiment scores
    def get_sentiments(self):
        for d in self.dates:
            sentiment_sum = 0

            for text in dates[d]:
                score = TextBlob(text).sentiment.polarity
                sentiment_sum += score

            try:
                self.sentiments[d] = sentiment_sum / float(self.counts[d])
            except:
                self.sentiments[d] = 0

        return [self.sentiments[k] for k in sorted(self.sentiments)]

	# function that writes all of the data to a file 
    def write_stats(self, f_counts, f_sentiments):
        count_list = self.get_counts()
        line1 = "{}\n".format(",".join(map(str, count_list)).strip())

        sentiment_list = self.get_sentiments()
        line2 = "{}\n".format(",".join(map(str, sentiment_list)).strip())

        f_counts.write(line1)
        f_sentiments.write(line2)

# function that opens the files containing the data
def get_files(movie):
    files = ["Counts/{}".format(movie), "Sentiments/{}".format(movie)]

    open_files = list()

    for f in files:

        if not os.path.isfile(f):
            os.system("touch {}".format(f))

        open_files.append(open(f, "w"))

    return open_files

# function that creates the date range given a start and end data
def date_range(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# function that returns the release dates, tweet counts, and tweet sentiment scores
def get_dates():
    start_date = date(2017, 3, 1)
    end_date = date(2018, 3, 5)

    dates = dict()
    counts = dict()
    sentiments = dict()

    for single_date in date_range(start_date, end_date):
        d = single_date.strftime("%Y-%m-%d")
        dates[d] = list()
        counts[d] = 0
        sentiments[d] = 0

    return dates, counts, sentiments


movie = sys.argv[1].strip()

print "{}: started".format(movie)

dates, counts, sentiments = get_dates()

f_counts, f_sentiments = get_files(movie)

m = Movie(dates, counts, sentiments)

path = os.path.join("Data", movie)

for line in open(path):
    m.add_tweet(line.strip())

m.write_stats(f_counts, f_sentiments)

f_counts.close()
f_sentiments.close()

print "{}: done".format(movie)
