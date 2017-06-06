from datetime import datetime
import json
datetime_object = datetime.strptime('Sun Mar 12 05:15:25 +0000 2017', '%a %b %d %H:%M:%S +0000 %Y').date()
# print(str(datetime_object))

# sort location to be used
allowed_location =['Austin, TX','Boston, MA','Chicago, IL','Dallas, TX','Denver, CO','Houston, TX','Los Angeles, CA','Maryland, USA','San Diego, CA','San Francisco, CA','Seattle, WA']
allowed_location_dict = dict();
allowed_location_dict["Austin, TX"] = "Austin_TX";
allowed_location_dict['Boston, MA'] = 'Boston_MA';
allowed_location_dict['Chicago, IL'] = 'Chicago_IL';
allowed_location_dict['Dallas, TX'] = 'Dallas_TX';
allowed_location_dict['Denver, CO']= 'Denver_CO';
allowed_location_dict['Houston, TX']='Houston_TX';
allowed_location_dict['Los Angeles, CA']='Los_Angeles_CA';
allowed_location_dict['Maryland, USA']='Maryland_USA';
allowed_location_dict['San Diego, CA']='San_Diego_CA';
allowed_location_dict['San Francisco, CA']='San_Francisco_CA';
allowed_location_dict['Seattle, WA']='Seattle_WA';

# read from the broken files and store them in a dictionary
filename = "newbk"
tweets_data = []
tweets_file = open(filename, "r", encoding="utf-8")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        pass
tweets_file.close()

from collections import defaultdict
dict_time_location = dict()
dict_time_location['2017-03-12'] = defaultdict(lambda : [])
dict_time_location['2017-03-11'] = defaultdict(lambda : [])
dict_time_location['2017-03-10'] = defaultdict(lambda : [])
dict_time_location['2017-03-09'] = defaultdict(lambda : [])
dict_time_location['2017-03-08'] = defaultdict(lambda : [])
dict_time_location['2017-03-07'] = defaultdict(lambda : [])

for tweet in tweets_data:
    try:
        if tweet['user']['location'] in allowed_location:
            datetime_object = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y').date()
            datetime_object = str(datetime_object)
            temp = dict_time_location[datetime_object][tweet ['user']['location']]
            temp.append(tweet['text'])
    except:
        # print("locha", tweet['text'])
        pass


for key in dict_time_location:
    for location in dict_time_location[key]:
        location_to_write = "..\\"+key+"\\"+allowed_location_dict[location]+".txt"
        tweets_text = dict_time_location[key][location]
        content = ""
        for tweet_text in tweets_text:
            content += tweet_text+"\n"
        # print(location_to_write)
        f = open(location_to_write, "a", encoding='utf-8')
        f.write(content)
        f.close()

# later create directory based on the dates and store location based files in them
# Historical data for locations
# generate temp graph for them
