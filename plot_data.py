from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def plot_clean_data(df):
    plt.figure(figsize=(8, 5))

    df.hist(figsize=(15,5), bins = 10, edgecolor='black')
    plt.suptitle('Histogram of all columns', fontsize=15)
    plt.show()


    df[['Model_Year', 'Fuel_Type']].hist(figsize=(10, 5), bins=15, edgecolor='black')
    plt.show()

if __name__ == '__main__':
    plot_data=copy_data('training.csv')
    plot_clean_data(plot_data)