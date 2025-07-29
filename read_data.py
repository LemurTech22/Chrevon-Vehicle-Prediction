import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def plot_data(df):
    df.info()
    sns.pairplot(df)
    plt.title('Pairplot of Features')
    plt.show()
    
def visualize_histogram(df):
    df.hist(figsize=(10, 10))
    plt.title('Histogram of Numerical Features')
    plt.tight_layout()

def main():
    data = pd.read_csv('training.csv')
    plot_data(data)
    visualize_histogram(data)
    plt.show()

if __name__ == '__main__':
    main()

