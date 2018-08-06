from collections import defaultdict

# function that opens the file and parses the information from the different data files
def process_file(d, filename):
    lines = map(str.strip, open(filename).readlines())

    for line in lines:
		# if statement that parses the tweet counts and sentiments from the corresponding files
        if filename in ["sentiments.csv", "counts.csv"]:
            movie, ratio = line.split()
            k = filename.split('.')[0]
            d[movie][k] = ratio
		# if statement that parses the critic review score, user review score, and release dates from the corresponding file
        elif filename == "reviewsAndDates.txt":
            movie, critics, user, rd = line.split()
            d[movie]["critics"] = critics
            d[movie]["user"] = user
            d[movie]["rd"] = rd
		# if statement that parses the lifetime gross and theater count from the corresponding file
        elif filename == "boxoffice.txt":
            movie = line.split()[0].split('#')[0]
            boxoffice, theaters = line.split()[-2:]
            d[movie]["boxoffice"] = boxoffice
            d[movie]["theaters"] = theaters


# function that prints all of the data for each movie 
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

        print line


if __name__ == "__main__":
    files = ["counts.csv", "sentiments.csv", "reviewsAndDates.txt", "boxoffice.txt"]
    nominees = set(["moonlight", "arrival", "fences", "hidden-figures", "hell-or-high-water", "hacksaw-ridge", "la-la-land", "manchester-by-the-sea", "lion"])
    movies = defaultdict(dict)

    for f in files:
        process_file(movies, f)

    print_data(movies, nominees)
