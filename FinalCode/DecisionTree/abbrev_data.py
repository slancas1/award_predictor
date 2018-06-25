
f = "2017.csv"
lines = map(str.strip, open(f).readlines())

for line in lines:
    fields = line.split(",")
    movie = fields[0]
    boxoffice = fields[2]
    theaters = fields[4]
    rd = fields[3]
    count = fields[7]
    _class = fields[-1]

    print "{},{},{},{},{}".format(movie, theaters, count, rd, _class)
