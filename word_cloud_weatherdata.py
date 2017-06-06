import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import *

def load_words_from_file(path_to_file):
    sw_set = set()
    with open(path_to_file, 'r') as f:
        [sw_set.add(word) for line in f for word in line.split()]
    return sw_set


text = ""
for i in range(1,37):
    file_name = "data_"+str(i)
    text += open(file_name, "r", encoding="utf-8").read()


UniNE_sw = load_words_from_file('englishST.txt')
wc = WordCloud(width =1600 ,height=800,stopwords=UniNE_sw).generate(text)
plt.title("fi")
wc.to_file("figure.png")
plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")

