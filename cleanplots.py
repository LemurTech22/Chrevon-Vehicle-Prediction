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

    def specialized_boxplots(self):
        sns.boxplot(x='Vehicle Category',y='Vehicle Population',data=self.df)
        plt.title('Vehicle Category vs Population percentage')
        plt.xlabel('Vehicle Category')
        plt.ylabel('Population')
        plt.show()

        sns.boxplot(x='Vehicle Category',y='Model Year',data=self.df)
        plt.title('Vehicle Category vs Population percentage')
        plt.xlabel('Vehicle Category')
        plt.ylabel('Population')
        plt.show()

        sns.boxplot(x='Vehicle Category',y='Vehicle Population', hue='Fuel Type',data=self.df)
        plt.title('Vehicle Category vs Population percentage')
        plt.xlabel('Vehicle Category')
        plt.ylabel('Population')
        plt.show()
