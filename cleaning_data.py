from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def replace_na(df):
    df = df.replace('Not Applicable', pd.NA)
    fuel_type_map= {
        'Gasoline': 0,
        'Diesel': 1,
        'Electric': 2,
        'Natural Gas': 3,
        'Hydrogen': 4
    }
    df['Fuel Type'] = df['Fuel Type'].map(fuel_type_map)
    
    return df.apply(pd.Series.unique)

if __name__ == '__main__':
    copy=copy_data('training.csv')
    print(replace_na(copy))

    #seperate each fuel type into gas 0 1 2 etc...
    #plot vehicle type trends 
    #fill missing data 
    #plot