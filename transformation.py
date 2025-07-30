from imports import np

class data_transformation:
    def __init__(self,df):
        self.df = df
    
    def log_transformation(self):
        #self.df['log_electric_miles'] = np.log(self.df['Electric Mile Range']+1)

        self.df['log_vehicle_population'] = np.log(self.df['Vehicle Population']+1)
        self.df['log_fuel_type'] = np.log(self.df['Fuel Type']+1)
        self.df['log_fuel_tech'] = np.log(self.df['Fuel Technology']+1)

    def transformed_data(self):
        self.log_transformation()
        return self.df