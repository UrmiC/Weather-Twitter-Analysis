import json
import sys
from collections import defaultdict
import pprint as pp

import os.path
for dirpath, dirnames, filenames in os.walk(".\\twitter_data"):
     i = 0
     for filename in filenames:
        filename = ".\\twitter_data\\"+filename
        print(filename)

        tweets_data = []
        tweets_file = open(filename, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                pass
        tweets_file.close()
        location_data_file_name = "location_"+str(i)
        location_tweet=defaultdict(lambda:[])
        for _tweet in tweets_data:
            try:
                temp=location_tweet[_tweet['user']['location']]
                temp.append(_tweet['text'])
            except:
                continue

        to_write = ""
        for key in location_tweet:
            if key is not None:
                to_write += "KEY "+key+":"
                for item in location_tweet[key]:
                    to_write += item
                to_write += "\n"

        f = open(".\location_data\\"+location_data_file_name, "w", encoding='utf-8')
        f.write(to_write)
        f.close()
        i+=1