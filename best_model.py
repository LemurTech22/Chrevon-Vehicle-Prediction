from imports import np
from pycaret.regression import *

class finding_best_model:
    def __init__(self,df):
        self.df = df
        self.s= RegressionExperiment()
        self.s.setup(self.df, target='Vehicle Population', session_id = 123, use_gpu=True)

    def finding_model(self):
        best = self.s.compare_models()
        self.s.evaluate_model(best)

        self.s.evaluate_model(best)
        #self.s.plot_model(best, plot='residuals')
        #self.s.plot_model(best, plot='feature')

        #self.s.save_model(best, 'best_pipeline')

    def Model(self):
        self.finding_model()
        self.s.compare_models()
