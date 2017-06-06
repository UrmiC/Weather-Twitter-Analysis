import json
import sys
from collections import defaultdict
import pprint as pp
from collections import defaultdict
import os.path
location_dict = defaultdict(lambda : [])
for dirpath, dirnames, filenames in os.walk(".\location_data"):
    i = 0
    for filename in filenames:
        filename = ".\location_data\\" + filename
        print(filename)
        location_file = open(filename, "r", encoding="utf-8")
        temp_list = []
        for line in location_file:
            if line.startswith("KEY"):
                index_tweet = line.find(":")
                dict_key = line[4:index_tweet].strip()
                line = line[index_tweet:]
                temp_list = location_dict[dict_key]
                temp_list.append(line)
            else:
                temp_list.append(line)

i = 0
for key in location_dict:
    to_write = ""
    location_file_name = "location_"+str(i)
    if key is not None:
        to_write += key+"\n"
        for item in location_dict[key]:
            to_write += item
        print("key ",key)
        if key != "":
            f = open(".\location_key_data\\"+location_file_name, "w", encoding='utf-8')
            f.write(to_write)
            f.close()
            i+=1

