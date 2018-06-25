
from collections import defaultdict


def process_file(d, filename):

    lines = map(str.strip, open(filename).readlines())

    for line in lines:

        if filename in ["sentiments.csv", "counts.csv"]:
            movie, ratio = line.split()
            k = filename.split('.')[0]
            d[movie][k] = ratio
        elif filename == "reviewsAndDates.txt":
            movie, critics, user, rd = line.split()
            d[movie]["critics"] = critics
            d[movie]["user"] = user
            d[movie]["rd"] = rd
        elif filename == "boxoffice.txt":
            movie = line.split()[0].split('#')[0]
            boxoffice, theaters = line.split()[-2:]
            d[movie]["boxoffice"] = boxoffice
            d[movie]["theaters"] = theaters


def print_data(d, n):

    for k1 in d:
        line = "movie"
        for k2 in d[k1]:
            line += "," + k2

        line += ",class"
        print line
        break

    for k1 in d:
        line = k1
        for k2 in d[k1]:
            line += "," + d[k1][k2]

        c = '1' if k1 in n else '0'
        line += "," + c

        # if c == '1':
        #     print line

        print line


if __name__ == "__main__":

    files = ["counts.csv", "sentiments.csv", "reviewsAndDates.txt", "boxoffice.txt"]
    nominees = set(["moonlight", "arrival", "fences", "hidden-figures", "hell-or-high-water", "hacksaw-ridge", "la-la-land", "manchester-by-the-sea", "lion"])
    movies = defaultdict(dict)

    for f in files:
        process_file(movies, f)

    print_data(movies, nominees)
