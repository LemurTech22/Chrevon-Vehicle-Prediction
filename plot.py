from imports import pd, plt,sns

class raw_visualizer:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def plot_data(self):
        self.df.info()
        sns.pairplot(self.df)
        plt.title('Pairplot of Features')
        plt.show()
        
    def visualize_histogram(self):
        self.df.hist(figsize=(10, 10))
        plt.title('Histogram of Numerical Features')
        plt.tight_layout()


