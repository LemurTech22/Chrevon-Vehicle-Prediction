from read_data import *

def copy_data(fileName):
    copy_df = pd.read_csv(fileName)
    return copy_df

def replace_NA(df):
    df = df.replace('Not Applicable', pd.NA)
    return df.info()

if __name__ == '__main__':
    copy=copy_data('training.csv')
    print(replace_NA(copy))