from DataPreparation.DataPreparation import DataPreparation
from Model.Estimator import Estimator

class Teams:
    model = None
    def __init__(self):
        if Teams.model is not None:
            return

        data = DataPreparation('TeamStories.csv', 'r', 'utf-16-le', '\t')
        self.data = data.GetData()

        self.learningEstimator = Estimator()
        Teams.model = self.learningEstimator.CreateModel(self.data)
        self.learningEstimator.Fit()        

    def GetTeams(self, text):
        predict = Teams.model.predict_proba([text])
        team_predict = list(zip(self.model.classes_, predict[0]))
        team_predict_sorted = sorted(team_predict, key=lambda x: x[1], reverse=True)

        return team_predict_sorted
