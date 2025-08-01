from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_log_error, mean_absolute_error


class Model_Creation:
    def __init__(self, df):
        self.df= df
        self.copy_df = df.copy()

    def split_data(self):
        features = self.copy_df.drop(columns=['Vehicle Population','Electric Mile Range'])
        target = self.copy_df['Vehicle Population']
        self.x_train,  self.x_test, self.y_train, self.y_test = train_test_split(features, target, test_size=0.25)


    def model_pipeline(self):

        self.model_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', RobustScaler()),
            ('etr', ExtraTreesRegressor(random_state=42))
        ])

        self.model_pipeline.fit(self.x_train, self.y_train)

    def model_predictions(self):

        predictions = self.model_pipeline.predict(self.x_test)
        self.mse = mean_squared_error(self.y_test, predictions)
        self.msle = mean_squared_log_error(self.y_test, predictions)
        self.mae = mean_absolute_error(self.y_test, predictions)
        self.r2 = r2_score(self.y_test, predictions)

    def show_results(self):

        print("Mean Squared Error: ",self.mse)
        print("Mean Squared Log Error: ",self.msle)
        print("Mean Absolute Error: ",self.mae)
        print("R2 Score: ",self.r2)

    def execute(self):
        self.split_data()
        self.model_pipeline()
        self.model_predictions()
        self.show_results()

        

