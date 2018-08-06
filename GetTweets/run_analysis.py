#!/usr/bin/env python2.7

import subprocess
import sys
import signal
import commands
import os

# function that creates a list of all the movie data
def get_movies():
	movies = list()

	for f in os.listdir("Data"):
		movies.append(f.strip())

	return movies
 
def signal_handler(signal, frame):
	processes = map(str.strip, commands.getstatusoutput("ps x")[1].split('\n')[1:])

	kill_string = "kill -9"

	for p in processes:
		if "python get_tweets.py" in p:
			pid = p.split()[0]
			kill_string += " " + pid

	if len(kill_string.split()) > 2:
		os.system(kill_string)

	sys.exit(0)



movies = get_movies()

for movie in movies:
	subprocess.Popen(["python", "get_averages.py", movie])

signal.signal(signal.SIGINT, signal_handler)

running = True

while running:
	pass
