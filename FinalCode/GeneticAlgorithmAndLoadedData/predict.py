# Alex Ayala
# Sophie Lancaster
# Aidan Lewis

import random
import operator
from datetime import date, datetime


dataFile = open("new_alex_data.csv")
movieFile = open("movieTitles2017.txt")

random.seed(datetime.now())

scores = []
movies = {}
dates = {}
userRatings = {}
criticRatings = {}
sentiment = {}
tweetCount = {}
lifetimeGross = {}
numberOfTheaters = {}
goldenGlobes = {}
criticsChoice = {}
yearBegin = date(2016, 1, 1)
first = True

class paramSet:
    def __init__(self, user, critic, sent, gross, theater, count, rd, criticAward, golden):
        self.userMult = user
        self.criticMult = critic
        self.sentMult = sent
        self.grossMult = gross
        self.theaterMult = theater
        self.countMult = count
        self.dateMult = rd
        self.goldenMult = golden
        self.criticAwardMult = criticAward
        self.scores = {}
        self.nominees = []
        self.sortedScores = []
        self.winner = ''
        self.fitness = 0

    def computeScores(self):
        for k in movies:
            self.scores[k] = (self.userMult*userRatings[k]+self.criticMult*criticRatings[k]+self.sentMult*sentiment[k] +
                              self.grossMult*lifetimeGross[k]+ self.theaterMult*numberOfTheaters[k]+self.countMult *
                               tweetCount[k]+self.dateMult*dates[k]+self.criticAwardMult*criticsChoice[k] + self.goldenMult*goldenGlobes[k])

        self.sortedScores = sorted(self.scores.iteritems(), key=operator.itemgetter(1))
        print self.sortedScores
        self.nominees = [n[0] for n in self.sortedScores[-20:]]
        self.winner = self.nominees[-1]

    def __str__(self):
        paramString = "userMult: {}\ncriticMult: {}\nsentMult: {}\ngrossMult: {}\ntheaterMult: {}\ncountMult: {}\ndateMult: {}\nFitness:  {}\n".format(self.userMult, self.criticMult, self.sentMult, self.grossMult, self.theaterMult, self.countMult, self.dateMult, self.fitness)
        paramString = paramString + "Golden Globes: {}\nCritic's Choice: {}\nWinner: {}\nNominees: {}\n".format(self.goldenMult, self.criticAwardMult, self.winner, self.nominees)
        return paramString

for line in movieFile:
    line = line.strip().split('#')
    movies[line[0]] = line[1]

for line in dataFile:
    line = line.strip().split(",")
    if first:
        first = False
        continue
    if line[1] == "NULL":
        criticRatings[line[0]] = 0
    else:
        criticRatings[line[0]] = int(line[1])

    if line[2] == "NULL":
        lifetimeGross[line[0]] = 0
    else:
        lifetimeGross[line[0]] = float(line[2])/1000. #int(line[2])/1000000000.

    if line[3] == "NULL":
        dates[line[0]] = 0
    else:
        month, day, year = map(int, line[3].split("/"))
        releaseDate = date(year, month, day)
        delta = releaseDate-yearBegin
        dates[line[0]] = delta.days/365.0 # Added 365 to normalize?
        #dates[line[0]] = int(line[3])
    if line[4] == "NULL":
        numberOfTheaters[line[0]] = 0
    else:
        numberOfTheaters[line[0]] = int(line[4])

    if line[5] == "NULL":
        sentiment[line[0]] = 0
    else:
        sentiment[line[0]] = float(line[5])

    if line[6] == "NULL":
        userRatings[line[0]] = 0
    else:
        userRatings[line[0]] = float(line[6])

    if line[7] == "NULL":
        tweetCount[line[0]] = 0
    else:
        tweetCount[line[0]] = float(line[7])

    if line[9] == "NULL":
        criticsChoice[line[0]] = 0
    else:
        criticsChoice[line[0]] = int(line[9])

    if line[10] == "NULL":
        goldenGlobes[line[0]] = 0
    else:
        goldenGlobes[line[0]] = int(line[10])

params = paramSet(-2.04529602987, 3.58677554026, 3.60802131784, -6.3138135618, 0.0148526973376,
                 -1.31409237727, 9.47295805662, 7.09437124458, 8.21434314202)
#params = paramSet(-8.68062878462, 0.655583750887, 0.272055593674, -9.55888213033, 0.0211656468326,
 #                 3.46734740166, 8.09562388019, 9.93304840944, 7.84450702783)

params.computeScores()

print params
print params.winner
print params.nominees
