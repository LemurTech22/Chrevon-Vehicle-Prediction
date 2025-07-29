from plot import raw_visualizer
from cleaning_data import DataCleaner
from cleanplots import DataVisualizer



def main():

    raw_data = raw_visualizer('training.csv')

    raw_data.plot_data()
    raw_data.visualize_histogram()

    cleaner = DataCleaner(raw_data.df)
    cleaned_data = cleaner.get_cleaned_data()

    visualizer = DataVisualizer(cleaned_data)
    visualizer.plot_data()
    visualizer.visualize_histogram()
    visualizer.specialized_histogram()

if __name__ == '__main__':
    main()