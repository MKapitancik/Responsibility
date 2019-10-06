from DataPreparation.DataPreparation import DataPreparation
from Model.Estimator import Estimator

data = DataPreparation('TeamStories.csv', 'r', 'utf-16-le', '\t')
data = data.GetData()

learningEstimator = Estimator()
model = learningEstimator.CreateModel(data)
scores = learningEstimator.EvaluateCrossValidationScore(5)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))    

learningEstimator.Fit()

while True:
    txt = input("Predict for:")

    if txt is 'Q':
        break
    
    predict = model.predict_proba([txt])
    team_predict = list(zip(model.classes_, predict[0]))
    team_predict_sorted = sorted(team_predict, key=lambda x: x[1], reverse=True)
    [print(team) for team in team_predict_sorted[:3]]