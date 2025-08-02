from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_log_error, mean_absolute_error, classification_report, accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Model_Creation:
    def __init__(self, df):
        self.df= df
        self.copy_df = df.copy()

    def drop_highly_correlated(self):
        
        print("\n🔍 Dropping highly correlated features...")
        self.copy_df.drop(columns=['Fuel Type'], inplace=True)   


    def split_data(self):
        self.features = self.copy_df.drop(columns=['Vehicle Population','Electric Mile Range'])
        self.target = self.copy_df[['Vehicle Population', 'Vehicle Category']]
        self.x_train,  self.x_test, self.y_train, self.y_test = train_test_split(self.features, self.target, test_size=0.25, stratify=self.target['Vehicle Category'])

        corr = self.copy_df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.show()
    
    def model_pipeline(self):

        self.model_regression_pipeline = Pipeline([
            ('imputer', IterativeImputer()),
            ('scaler', RobustScaler()),
            ('etr', RandomForestRegressor(n_estimators=50,
                                            max_depth=5,           # shallow trees to reduce overfitting
                                            min_samples_split=10,  # minimum samples per split
                                            min_samples_leaf=5,    # minimum samples per leaf
                                            random_state=42))
        ])
        self.model_classifier_pipeline = Pipeline([
            ('imputer', IterativeImputer()),
            ('scaler', RobustScaler()),
            ('clf', RandomForestClassifier(n_estimators=50,
                                            max_depth=5,           # shallow trees to reduce overfitting
                                            min_samples_split=10,  # minimum samples per split
                                            min_samples_leaf=5,    # minimum samples per leaf
                                            random_state=42))
        ])
        
        self.model_regression_pipeline.fit(self.x_train, self.y_train['Vehicle Population'])
        self.model_classifier_pipeline.fit(self.x_train, self.y_train['Vehicle Category'])

        scores = cross_val_score(self.model_classifier_pipeline, self.features, self.target['Vehicle Category'], cv=5)
        print("Cross-validated accuracy:", scores.mean())

    def model_predictions(self):

        self.predictions_regression = self.model_regression_pipeline.predict(self.x_test)
        self.mse = mean_squared_error(self.y_test['Vehicle Population'], self.predictions_regression)
        self.msle = mean_squared_log_error(self.y_test['Vehicle Population'], self.predictions_regression)
        self.mae = mean_absolute_error(self.y_test['Vehicle Population'], self.predictions_regression)
        self.r2 = r2_score(self.y_test['Vehicle Population'], self.predictions_regression)

        self.predictions_classifier = self.model_classifier_pipeline.predict(self.x_test)


    def show_results(self):

        print("Mean Squared Error: ",self.mse)
        print("Mean Squared Log Error: ",self.msle)
        print("Mean Absolute Error: ",self.mae)
        print("R2 Score: ",self.r2)

        print(classification_report(self.y_test['Vehicle Category'], self.predictions_classifier))
        print('Accuracy Score: ',accuracy_score(self.y_test['Vehicle Category'], self.predictions_classifier))

    def convert_to_dataframe(self):
        result_df = pd.DataFrame({
        'Actual Population': self.y_test['Vehicle Population'].values,
        'Predicted Population': self.predictions_regression,
        'Actual Category': self.y_test['Vehicle Category'].values,
        'Predicted Category': self.predictions_classifier
    })
        
        print(result_df.head(20))

    def execute(self):
        self.drop_highly_correlated()
        self.split_data()
        self.model_pipeline()
        self.model_predictions()
        self.show_results()
        self.convert_to_dataframe()
