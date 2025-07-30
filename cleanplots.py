from imports import plt,sns,np

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

        self.df['Vehicle Category'].hist(bins=30)
        plt.title('Count of Vehicle Category')
        plt.xlabel('Vehicle Category')
        plt.ylabel('Frequency')
        plt.show()

        self.df['Model Year'].hist(bins=30)
        plt.title('Count of different Model Years')
        plt.xlabel('Model Year')
        plt.ylabel('Frequency')
        plt.show()
        
        self.df['Electric Mile range'].hist(bins=30)
        plt.title('Count of Electric Mile Range')
        plt.xlabel('Electric Mile Range')
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

        sns.boxplot(x='GVWR Class', y='Vehicle Category', data=self.df)
        plt.title('GVWR Class vs Vehicle Category')
        plt.xlabel('GVWR Class')
        plt.ylabel('Vehicle Category')
        plt.show()

    def distrubtion_plot(self):

        sns.kdeplot(data = self.df, x= 'Vehicle Category',fill=True)
        plt.title('KDE plot of Vehicle Category')
        plt.xlabel('Vehicle Category')
        plt.ylabel('Density')
        plt.show()

        sns.kdeplot(data = self.df, x='Vehicle Population',fill=True)
        plt.title('KDE plot of Vehicle Population')
        plt.xlabel('Vehicle Population')
        plt.ylabel('Density')
        plt.show()


    def heatmap_plot(self):
        corr_matrix=self.df.select_dtypes(include=[np.number]).corr()

        print(corr_matrix)

        sns.heatmap(corr_matrix, annot=True)
        plt.title('Linear Correlation')
        plt.show()

