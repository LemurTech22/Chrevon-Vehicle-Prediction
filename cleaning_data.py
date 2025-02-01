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
    df['Fuel Type'] = df['Fuel Type'].map(fuel_type_map)
    df = df.drop('Region', axis=1)
    df.drop(columns=['Number of Vehicles Registered at the Same Address'], errors='ignore', inplace=True)

    df.to_csv('unit_Testing.csv')
    return print('test')



if __name__ == '__main__':
    copy=copy_data('training.csv')
    print(replace_na(copy))

    #seperate each fuel type into gas 0 1 2 etc...
    #plot vehicle type trends 
    #fill missing data 
    #plot