from imports import np
from pycaret.regression import *

class finding_best_model:
    def __init__(self,df):
        self.df = df
        self.s= RegressionExperiment()
        self.s.setup(self.df, target='Vehicle Population', session_id = 123)

    def finding_model(self):
        best = self.s.compare_models()
        self.s.evaluate_model(best)

        #holdout = self.s.predict_model(best)
        new_data = self.df.copy().drop('Vehicle Population', axis=1)
        prediction = self.s.predict_model(best, data=new_data)

        self.s.evaluate_model(best)
        self.s.plot_model(best, plot='residuals')
        self.s.plot_model(best, plot='feature')

        #self.s.save_model(best, 'best_pipeline')

    def Model(self):
        self.finding_model()
        self.s.compare_models()
