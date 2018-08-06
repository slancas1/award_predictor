# this file goes through and adds a 1 if the movie was a previous nominee and a 0 if it wasn't (adds two new columns to the file for the different awards shows)
goldenglobes = ["20th-century-women", "deadpool", "hacksaw-ridge", "hell-or-high-water", "lion", "florence-foster-jenkins", "manchester-by-the-sea", "moonlight", "sing-street", "la-la-land"]

criticschoice = ["la-la-land", "arrival", "fences", "hacksaw-ridge", "hell-or-high-water", "lion", "loving", "manchester-by-the-sea", "moonlight", "sully"]


lines = map(str.strip, open("new_data.csv").readlines())

print lines[0] + ",goldenglobes,criticschoice"

for line in lines[1:]:

    movie = line.split(",")[0]

    gg = '1' if movie in goldenglobes else '0'
    cc = '1' if movie in criticschoice else '0'

    print "{},{},{}".format(line, gg, cc)
