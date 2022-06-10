import requests

import re

import seaborn as sns
url= "https://en.wikipedia.org/w/api.php"
res = requests.get(url, params={"action":"query", "prop": "extracts", "titles":"Ozone_layer", "format":"json"})
json_data = res.json()
raw_text = json_data['query']['pages']['22834']['extract']
def cleanhtml(raw_html):
    html = re.compile('<.*?>')
    clean = re.sub(html,'',raw_html)
    return clean
no_html_text = cleanhtml(raw_text)
def merge_contents(data):
    splitted_text = re.split("\. |, |\. |\n| |- |\'", data)
    return splitted_text
merge_content = merge_contents(no_html_text)
def tokenize(content):
    special_char_removed = [word for word in content if word.isalnum()]
    num_removed = [word for word in special_char_removed if not word.isdigit()]
    return num_removed

collection = tokenize(merge_content)


def lower_collection(collection):
    return [word.lower() for word in collection]


plain_text = lower_collection(collection)
def count_frequency(collection):
    frequency = {}
    for word in collection:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
freq_of_words = count_frequency(plain_text)
freq_of_words = {k:v for k,v in sorted (freq_of_words.items(), key=lambda item: item[1], reverse=True)}
xx = [v for k,v in freq_of_words.items() ]
yy = [k for k,v in freq_of_words.items() ]
sns.barplot(x=xx[0:20], y=yy[0:20])
stop_words = ['the', 'of', 'and', 'in', 'to', 'is', 'a', 'an'
              'by', 'that', 'for', 'was', 'were', 'are',
              'from', 'at', 'it', 'as', 'be', 'these', 'on', 'with', 'this', 'have', 'has', 'other',
              'because', 'can', 'its', 'out', 'about', 'into', 'or', 'over', 'all', 'most', 'which', 'less', 'while', 'above',
              'than', 's', 'a', 'b']
meaningful_text = [word for word in plain_text if word not in stop_words]
freq_of_meaningful_words = count_frequency(meaningful_text)
freq_of_meaningful_words = freq_of_words = {k:v for k,v in sorted (freq_of_meaningful_words.items(), key=lambda item: item[1], reverse=True)}
xxx = [v for k,v in freq_of_meaningful_words.items() ]
yyy = [k for k,v in freq_of_meaningful_words.items() ]
a = sns.barplot(x=xxx[0:20], y=yyy[0:20])
print(a)