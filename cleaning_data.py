from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def replace_na(df):
    
    df = df.replace('Not Applicable', pd.NA)
    df = df.replace('Unknown', pd.NA)

    msno.bar(df)
    msno.heatmap(df)
    plt.show()
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

    missing_row = df[df['Fuel_Type'].isnull()]

    df = df.dropna(subset=['Fuel_Type'])
    print(missing_row)

    print('Unique Values', df['vehicle_category'].unique())
    return df

def rename_df(df):
    col = {'Vehicle Category': 'vehicle_category', 'GVWR Class': 'GVWR_Class', 'Fuel Type':  'Fuel_Type', 
           'Model Year': 'Model_Year','Fuel Technology': 'Fuel_Technology', 'Electric Mile Range': 'Electric_Mile_Range', 
           'Number of Vehicles Registered at the Same Address': 'Number_of_Vehicles_Registered_at_the_Same_Address', 
           'Vehicle Population': 'Vehicle_Population'}
    df.rename(columns=col,inplace =True)
    print(df)
    return df

def split_df(df):

    # Assuming Fuel_Type is mapped: Gasoline=0, Diesel=1, etc.
    gasoline_df = df[df['Fuel_Type'] == 0]
    diesel_df = df[df['Fuel_Type'] == 1]
    electric_df = df[df['Fuel_Type'] == 2]
    natural_gas_df = df[df['Fuel_Type'] == 3]
    hydrogen_df = df[df['Fuel_Type'] == 4]

    natural_gas_df.drop(columns ='Electric_Mile_Range', errors='ignore', inplace=True)
    diesel_df.drop(columns ='Electric_Mile_Range', errors='ignore', inplace=True)

    return gasoline_df,diesel_df, electric_df, natural_gas_df,hydrogen_df


def replace_GVWR_Class(df):
    
    return df
  
if __name__ == '__main__':
    copy = copy_data('training.csv')
    copy = rename_df(copy)
    copy = replace_na(copy)
    #plot_data(copy)
    copy = replace_GVWR_Class(copy)
    gas_df, dis_df, elec_df, nat_gas_df, hydro_df = split_df(copy)
    

    print('Gas electric Mile range',gas_df['Electric_Mile_Range'].value_counts())

    print('Eletric electric Mile range',elec_df['Electric_Mile_Range'].value_counts())
        
    print('Hydrogen electric Mile range',hydro_df['Electric_Mile_Range'].value_counts())

    gas_df.to_csv('gas_df.csv')
    elec_df.to_csv('elec_df.csv')
    hydro_df.to_csv('hydro_df.csv')

'''

# Let's assume the column with vehicle types is 'vehicle_type' and the column with data is 'value_column'

# You can calculate the mean for each vehicle type
grouped_means = df.groupby('vehicle_type')['value_column'].mean()

# Replace NaN values in 'value_column' with the corresponding type's mean
def replace_with_group_mean(row):
    if pd.isna(row['value_column']):
        # Use the group mean for that vehicle type
        return grouped_means[row['vehicle_type']]
    return row['value_column']

# Apply the function to the DataFrame
df['value_column'] = df.apply(replace_with_group_mean, axis=1)
'''