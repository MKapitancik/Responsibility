from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split, cross_val_score

class Estimator:
    def CreateModel(self, data):
        self.values = []
        self.target = []

        for d in data:
            team = d[2]    
            summary = d[1]
            self.values.append(summary)
            self.target.append(team)
            #print('{0:10} {1}'.format(team, summary))

        self.model = make_pipeline(TfidfVectorizer(stop_words=set(stopwords.words('english')), sublinear_tf=True, ngram_range=(1, 2), min_df=2, max_df=0.95), MultinomialNB())
        #model = make_pipeline(CountVectorizer(stop_words=set(stopwords.words('english')), ngram_range=(1, 2), min_df=2, max_df=0.95), MultinomialNB())

        return self.model

    def Fit(self):
        self.model.fit(self.values, self.target)

    def EvaluateCrossValidationScore(self, cv):
        return cross_val_score(self.model, self.values, self.target, cv=cv)    