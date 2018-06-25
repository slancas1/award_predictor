# Alex Ayala
# Sophie Lancaster
# Aidan Lewis

import time
import random
import operator
from datetime import date, datetime


dataFile = open("new_all_data.csv")
movieFile = open("newMovies.txt")

winner = "moonlight-2016"
nominees = ["moonlight-2016", "arrival", "fences", "hacksaw-ridge", "hell-or-high-water", "hidden-figures",
            "la-la-land", "lion", "manchester-by-the-sea"]

random.seed(datetime.now())

population = []

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
generations = 700
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
        self.nominees = [n[0] for n in self.sortedScores[-20:]]
        self.winner = self.nominees[-1]

    def computeFitness(self):
        self.computeScores()
        self.fitness = 0
        for ind, nom in enumerate(self.sortedScores):
            if nom[0] in nominees:
                if ind >= len(self.sortedScores)-10:
                    self.fitness += ind
                else:
                    self.fitness -= (len(self.sortedScores) - ind)
            if nom[0] not in nominees and ind >= len(self.sortedScores) - 10:
                #self.fitness -= 1.5*ind
                self.fitness -= ind
                self.fitness -= 50
            if nom[0] == winner:
                #self.fitness += 1.5*ind
                #self.fitness += ind
                #self.fitness += 50
                if ind == len(self.sortedScores)-1:
                    #self.fitness += ind
                    self.fitness += ind
                    self.fitness += 100
                # Added
                elif ind >= len(self.sortedScores)-10:
                    self.fitness += ind
                    #self.fitness -= 50
                else:
                    self.fitness -= (len(self.sortedScores) - ind)
                    self.fitness -= 50
            if nom[0] != winner and ind == len(self.sortedScores)-1:
                if nom[0] in nominees:
                    self.fitness -= ind
                else:
                    #self.fitness -= 1.5 * ind
                    self.fitness -= 50
                    self.fitness -= ind


    def __str__(self):
        paramString = "userMult: {}\ncriticMult: {}\nsentMult: {}\ngrossMult: {}\ntheaterMult: {}\ncountMult: {}\ndateMult: {}\nFitness:  {}\n".format(self.userMult, self.criticMult, self.sentMult, self.grossMult, self.theaterMult, self.countMult, self.dateMult, self.fitness)
        paramString = paramString + "Golden Globes: {}\nCritic's Choice: {}\nWinner: {}\nNominees: {}\n".format(self.goldenMult, self.criticAwardMult, self.winner, self.nominees)
        return paramString


def makeChildren(p1, p2):
    doMutate1 = random.random()
   # mutation1 = random.uniform(-3, 3)
    mutationSelector1 = [random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8)]
    doMutate2 = random.random()
  #  mutation2 = random.uniform(-3, 3)
    mutationSelector2 = [random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8)]
    #crossover = random.randint(0,8)
    crossover = [random.randint(0,1), random.randint(0,8), random.randint(0,8), random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8)]

    params1 = [p1.userMult, p1.criticMult, p1.sentMult, p1.grossMult, p1.theaterMult, p1.countMult, p1.dateMult, p1.criticAwardMult, p1.goldenMult]
    params2 = [p2.userMult, p2.criticMult, p2.sentMult, p2.grossMult, p2.theaterMult, p2.countMult, p2.dateMult, p2.criticAwardMult, p2.goldenMult]

    for c, cross in enumerate(crossover):
        if cross == 1:
            holder = params1[c]
            params1[c] = params2[c]
            params2[c] = holder

    user = params1[0]
    critic = params1[1]
    sent = params1[2]
    gross = params1[3]
    theater = params1[4]
    count = params1[5]
    rd = params1[6]
    cc = params1[7]
    gg = params1[8]

    user2 = params2[0]
    critic2 = params2[1]
    sent2 = params2[2]
    gross2 = params2[3]
    theater2 = params2[4]
    count2 = params2[5]
    rd2 = params2[6]
    cc2 = params2[7]
    gg2 = params2[8]

    if doMutate1 < .2:
        if 0 in mutationSelector1:
            user += random.uniform(-3, 3)
        elif 1 in mutationSelector1:
            critic += random.uniform(-3, 3)
        elif 2 in mutationSelector1:
            sent += random.uniform(-3, 3)
        elif 3 in mutationSelector1:
            gross += random.uniform(-3, 3)
        elif 4 in mutationSelector1:
            theater += random.uniform(-3, 3)
        elif 5 in mutationSelector1:
            count += random.uniform(-3, 3)
        elif 6 in mutationSelector1:
            rd += random.uniform(-3, 3)
        elif 7 in mutationSelector1:
            cc += random.uniform(-3, 3)
        elif 8 in mutationSelector1:
            gg += random.uniform(-3, 3)

    if doMutate2 < .2:
        if 0 in mutationSelector2:
            user2 += random.uniform(-3, 3)
        elif 1 in mutationSelector2:
            critic2 += random.uniform(-3, 3)
        elif 2 in mutationSelector2:
            sent2 += random.uniform(-3, 3)
        elif 3 in mutationSelector2:
            gross2 += random.uniform(-3, 3)
        elif 4 in mutationSelector2:
            theater2 += random.uniform(-3, 3)
        elif 5 in mutationSelector2:
            count2 += random.uniform(-3, 3)
        elif 6 in mutationSelector2:
            rd2 += random.uniform(-3, 3)
        elif 7 in mutationSelector2:
            cc2 += random.uniform(-3, 3)
        elif 8 in mutationSelector2:
            gg2 += random.uniform(-3, 3)

    child1 = paramSet(user, critic, sent, gross, theater, count, rd, cc, gg)
    child2 = paramSet(user2,critic2,sent2,gross2,theater2,count2,rd2, cc2, gg2)
    return child1, child2


def selectPairs(pop):
    #subpop = random.sample(pop, 100)
    #subpop.sort(key=operator.attrgetter('fitness'), reverse=True)
    #subpop = pop[:100]
    subpop = pop
    minimumFit = abs(subpop[-1].fitness)
    adjustedFitness = [a.fitness+2*minimumFit for a in subpop]
    total = sum(adjustedFitness)
    pick1 = random.uniform(0, total)
    pick2 = random.uniform(0, total)
    ind1 = 0
    ind2 = 0
    the_sum = 0
    for ind, par1 in enumerate(subpop):
        the_sum += adjustedFitness[ind]
        if pick1 < the_sum:
            ind1 = ind
            break

    the_sum = 0
    for ind, par2 in enumerate(subpop):
        the_sum += adjustedFitness[ind]
        if pick2 < the_sum:
            ind2 = ind
            break

    return subpop[ind1], subpop[ind2]

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
        lifetimeGross[line[0]] = int(line[2])/1000000000.

    if line[3] == "NULL":
        dates[line[0]] = 0
    else:
        month, day, year = map(int, line[3].split("/"))
        releaseDate = date(year, month, day)
        delta = releaseDate-yearBegin
        dates[line[0]] = delta.days/365.0 # Added 365 to normalize?

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


startTime = time.time()

for i in range(1000):
    population.append(paramSet(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10),
                               random.uniform(-10, 10),random.uniform(-10, 10),random.uniform(-10, 10),
                               random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)))

for j in range(generations):
    print j
    for k in population:
        k.computeFitness()
        if j % 10 == 0:
            print k.fitness, k.nominees

    parents1 = []
    parents2 = []
    population.sort(key=operator.attrgetter('fitness'), reverse=True)
    for l in range(150):
        parent1, parent2 = selectPairs(population)
        parents1.append(parent1)
        parents2.append(parent2)

    children = []
    for parent1, parent2 in zip(parents1, parents2):
        child1, child2 = makeChildren(parent1, parent2)
        children.append(child1)
        children.append(child2)

    population = population[:-300] + children

for k in population:
    k.computeFitness()

population.sort(key=operator.attrgetter('fitness'), reverse=True)

totalTime = time.time() - startTime

print totalTime
print population[0]