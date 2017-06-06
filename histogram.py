import matplotlib.pyplot as plt

keyword_value = ['cloud',
'cold',
'dry',
'hot',
'humid',
'rain',
'snow',
'sunny',
'wind',
'breezy']

keyword_index = [1,2,3,4,5,6,7,8,9,10]
import os
from collections import defaultdict



for dirpath, dirnames, filenames in os.walk(".\\..\\2017-03-07"):
    for filename in filenames:
        plt.title(filename)
        print(filename)
        filename = ".\\..\\2017-03-07\\" + filename
        location_file = open(filename, "r", encoding="utf-8")
        keyword_count = dict()
        for key in keyword_value:
            keyword_count[key] = 0
        for line in location_file:
            line_split = line.split(" ")
            for word in line_split:
                if word in keyword_value:
                    keyword_count[word] += 1

        keyword_count_value = []
        for key in keyword_value:
            keyword_count_value.append(keyword_count[key])

        plt.xlabel("Keywords")
        plt.ylabel("Count")
        print(keyword_count)
        plt.bar(keyword_index,keyword_count_value)
        plt.xticks(keyword_index, keyword_value)
        plt.show()

# select the files you want to process and store them in a list
# read the file line by line and maintain the dict to store the count of relevant key words
# once you have the count
# replace
# the plt.bar as  plt.bar([list of number of keywords], [count of keywords])
# plt.xticks as plt.xticks([list of keywords])