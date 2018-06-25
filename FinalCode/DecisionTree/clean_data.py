
lines = map(str.strip, open("all_data.csv").readlines())[1:]

for line in lines:
    fields = line.split(",")
    gross = int(fields[2]) / float(1000000)
    mon = fields[3].split("/")[0]

    print "{},{},{},{}".format(",".join(fields[:2]), gross, mon, ",".join(fields[4:]))
