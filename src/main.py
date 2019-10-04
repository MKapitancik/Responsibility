from random import shuffle

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from nltk.corpus import stopwords

from DataPreparation.FetchCommits import FetchCommits
from DataPreparation.TextNormalization import TextNormalization
from DataPreparation.TeamNameParser import TeamNameParser
from DataPreparation.DataCleaning import DataCleaning
from DataPreparation.ConvertToTypes import ConvertToTypes
from DataPreparation.TextOperations import TextOperations

c = FetchCommits(open, 'TeamStories.csv', 'r', 'utf-16-le', '\t')
data = c.Load()

typeConverter = ConvertToTypes(int, str, str)
data = typeConverter.Convert(data)
shuffle(data)

to = TextOperations()
storyOperations = TextNormalization()
storyOperations.SetStrategy(to.OnlyCharacters, to.RemoveCamelCase, to.SingleWhitespaces, to.StripEndWhitespaces, to.ToLower)

teamOperations = TextNormalization()
teamOperations.SetStrategy(to.OnlyCharacters, to.SingleWhitespaces, to.ToLower, TeamNameParser().Parse)

column_operations = {
    0 : None,
    1 : storyOperations.Normalize,
    2 : teamOperations.Normalize,
}

dc = DataCleaning(column_operations)
data = dc.Clean(data)

values = []
target = []

for d in data:
    team = d[2]    
    summary = d[1]
    values.append(summary)
    target.append(team)
    #print('{0:10} {1}'.format(team, summary))

model = make_pipeline(TfidfVectorizer(stop_words=set(stopwords.words('english')), sublinear_tf=True, ngram_range=(1, 2), min_df=2, max_df=0.95), MultinomialNB())
#model = make_pipeline(CountVectorizer(stop_words=set(stopwords.words('english')), ngram_range=(1, 2), min_df=2, max_df=0.95), MultinomialNB())
scores = cross_val_score(model, values, target, cv=5)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))    

model.fit(values, target)

while True:
    txt = input("Predict for:")

    if txt is 'Q':
        break
    
    predict = model.predict_proba([txt])
    team_predict = list(zip(model.classes_, predict[0]))
    team_predict_sorted = sorted(team_predict, key=lambda x: x[1], reverse=True)
    [print(team) for team in team_predict_sorted[:3]]
