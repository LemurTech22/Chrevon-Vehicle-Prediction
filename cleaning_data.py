from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def replace_na(df):
    df = df.replace('Not Applicable', pd.NA)
    df = df.replace('Unknown', pd.NA)

    fuel_type_map= {
        'Gasoline': 0,
        'Diesel': 1,
        'Electric': 2,
        'Natural Gas': 3,
        'Hydrogen': 4
    }
    df['Fuel_Type'] = df['Fuel_Type'].map(fuel_type_map)
    df = df.drop('Region', axis=1)
    df.drop(columns=['Number_of_Vehicles_Registered_at_the_Same_Address'], errors='ignore', inplace=True)

    return df

def rename_df(df):
    col = {'Vehicle Category': 'vehicle_category', 'GVWR Class': 'GVWR_Class', 'Fuel Type':  'Fuel_Type', 
           'Model Year': 'Model_Year','Fuel Technology': 'Fuel_Technology', 'Electric Mile Range': 'Electric_Mile_Range', 
           'Number of Vehicles Registered at the Same Address': 'Number_of_Vehicles_Registered_at_the_Same_Address', 
           'Vehicle Population': 'Vehicle_Population'}
    df.rename(columns=col,inplace =True)
    print(df)
    return df

if __name__ == '__main__':
    copy = copy_data('training.csv')
    copy = rename_df(copy)
    copy = replace_na(copy)

    copy.info()



