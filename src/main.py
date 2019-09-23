from DataPreparation.FetchCommits import FetchCommits
from DataPreparation.TextNormalization import TextNormalization
from DataPreparation.TeamNameParser import TeamNameParser
from DataPreparation.DataCleaning import DataCleaning
from DataPreparation.TextOperations import *
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing

c = FetchCommits(open, 'TeamStories.csv', 'r', 'utf-16-le', '\t')
data = c.Load()
to = TextOperations()
textNormalization = TextNormalization([to.OnlyCharacters, to.SingleWhitespaces, to.StripEndWhitespaces, to.RemoveCamelCase, to.ToLower])

dc = DataCleaning(textNormalization, TeamNameParser())

data = dc.Clean(data)

split = [d[1].split() for d in data]

words = [item.lower() for sublist in split for item in sublist if len(item) > 4]

wordsCount = Counter(words)

# print(wordsCount.most_common(20))
# print("most uncommon:")
# print(list(wordsCount.items())[-20:])

teamWords = {}
for d in data:
    key = d[2]    
    values = d[1]
    if (key in teamWords):
        teamWords[key] += ' ' +  values  #[v for v in values.split() if len(v) > 2]
        continue
    teamWords[key] = values #[v for v in values.split() if len(v) > 2]

# for key, value in teamWords.items():
#     c = Counter(value)
#     print('Team: %s' % key, ' most common values : %s' % c.most_common(5))

values = []
target = []

for d in data:
    key = d[2]    
    val = d[1]
    values.append(val)
    target.append(key)

model = make_pipeline(TfidfVectorizer(sublinear_tf=True, ngram_range=(1, 2), stop_words='english'), MultinomialNB())
model.fit(values, target)

predict = model.predict_proba(['lion animal'])

team_predict = list(zip(model.classes_, predict[0]))
team_predict_sorted = sorted(team_predict, key=lambda x: x[1], reverse=True)
[print(team) for team in team_predict_sorted[:3]]


