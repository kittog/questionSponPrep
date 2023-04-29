# PREPROCESSING THE DATA


#### IMPORTATION DES MODULES
import string
from nltk.corpus import stopwords
import nltk
import re


#### NETTOYAGE DES QUESTIONS
# stopwords

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("french")
stopword = set(stopwords.words('french'))

def clean(question):
    question = str(question).lower()
    question = re.sub('\[.*?\]', '', question)
    question = re.sub('https?://\S+|www\.\S+', "", question)
    question = re.sub('<.*?>+', '', question)
    question = re.sub('[%s]' % re.escape(string.punctuation), '', question)
    question = re.sub('\n', '', question)
    question = re.sub('\w*\d\w*', '', question)
    question = [word for word in question.split(' ') if word not in stopword]
    question = " ".join(question)
    question = [stemmer.stem(word) for word in question.split(' ')]
    question = " ".join(question)
    return question


#### MAIN

data["question"] = data["question"].apply(clean)
data["previous_5_turn"] = data["previous_5_turn"].apply(clean)
data["next_5_turn"] = data["next_5_turn"].apply(clean)
