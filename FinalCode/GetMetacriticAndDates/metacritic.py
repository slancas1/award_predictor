#!/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import unirest

f = open("movieTitles2017.txt", "r")
out = open("reviewsAndDates2017.txt", "w")
for m in f:
    m = m.strip().split("#")
    print m[0]
    url = "https://api-marcalencc-metacritic-v1.p.mashape.com/movie/" + m[0] + "/{year}"
    url2 = "https://api-marcalencc-metacritic-v1.p.mashape.com/movie/" + m[0] + "/2017"

    try:
	    response = unirest.get(url, headers={
	        "X-Mashape-Key": "ACo6tjzn7mmsh5xorxKY7Lio7E9Sp1cLHVijsngoOfHxM5SA1V",
	        "Accept": "application/json"
	    }
            )
    except:
	    response = unirest.get(url2, headers={
	        "X-Mashape-Key": "ACo6tjzn7mmsh5xorxKY7Lio7E9Sp1cLHVijsngoOfHxM5SA1V",
	        "Accept": "application/json"
	    }
            )
	
    if u'Rating' in response.body[0]:
        line = m[0]
        if u'CriticRating' in response.body[0][u'Rating']:
            line = line + " " + str(response.body[0][u'Rating'][u'CriticRating']) + " "
        else:
            line = line + " NULL "
        if u'UserRating' in response.body[0][u'Rating']:
            line = line + str(response.body[0][u'Rating'][u'UserRating']) + " "
        else:
            line = line + "NULL "
        if u'ReleaseDate' in response.body[0]:
            line = line + str(response.body[0][u'ReleaseDate']) + "\n"
        else:
            line = line + "NULL\n"
        out.write(line.encode('utf8'))
    else:
        line = m[0] + " NULL NULL "
        if u'ReleaseDate' in response.body[0]:
            line = line + str(response.body[0][u'ReleaseDate']) + "\n"
        else:
            line = line + "NULL\n"
        out.write(line.encode('utf8'))

f.close()
out.close()
