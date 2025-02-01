from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def replace_na(df):
    
    df = df.replace('Not Applicable', pd.NA)
    df = df.replace('Unknown', pd.NA)

    msno.bar(df)
    msno.heatmap(df)
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

    missing = df['Fuel_Type'].isnull().sum()
    missing_row = df[df['Fuel_Type'].isnull()]

    df = df.dropna(subset=['Fuel_Type'])

    missing = df['Fuel_Type'].isnull().sum()

    print(missing_row)
    missing_row = df[df['Fuel_Type'].isnull()]

    print(f'Number of Missing fuel type: ', missing)
    #modify
    #df['GVWR_Class'] = np.where(df['Vehicle_Category']=='p',)
    return df
def replace_GVWR_Class(df):
    plt.figure(figsize=(8, 5))

    df.hist(figsize=(15,5), bins = 10, edgecolor='black')
    plt.suptitle('Histogram of all columns', fontsize=15)
    plt.show()


    df[['Model_Year', 'Fuel_Type']].hist(figsize=(10, 5), bins=15, edgecolor='black')
    plt.show()

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
    plot_data(copy)
    copy = replace_GVWR_Class(copy)
    #copy.to_csv('changes.csv')
    



