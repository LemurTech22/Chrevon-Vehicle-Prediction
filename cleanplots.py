from imports import plt,sns

class DataVisualizer:

    def __init__(self,df):
        self.df = df

    def plot_data(self):
        self.df.info()
        sns.pairplot(self.df)
        plt.title('Pairplot of Features')
        plt.show()
        
    def visualize_histogram(self):
        self.df.hist(figsize=(10, 10))
        plt.title('Histogram of Numerical Features')
        plt.tight_layout()
    def specialized_histogram(self):
        self.df['Vehicle Population'].hist(bins=30)
        plt.title("Distribution of Vehicle Population")
        plt.xlabel('Population')
        plt.ylabel('Frequency')
        plt.show()

