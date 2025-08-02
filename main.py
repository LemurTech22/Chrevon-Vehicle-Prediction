from plot import raw_visualizer
from cleaning_data import DataCleaner
from cleanplots import DataVisualizer
from transformation import data_transformation
from best_model import finding_best_model
from model_creation import Model_Creation

def main():

    raw_data = raw_visualizer('training.csv')

    #raw_data.plot_data()
    #raw_data.visualize_histogram()

    cleaner = DataCleaner(raw_data.df)
    cleaned_data = cleaner.get_cleaned_data()

    #visualizer = DataVisualizer(cleaned_data)
    #visualizer.plot_data()
    #visualizer.visualize_histogram()
    #visualizer.specialized_histogram()
    #visualizer.specialized_boxplots()
    #visualizer.distrubtion_plot()
    #visualizer.heatmap_plot()
    
    transform = data_transformation(cleaned_data)
    transformed_data = transform.transformed_data()
    
    transformed_plots = DataVisualizer(transformed_data)
    #transformed_plots.heatmap_plot()

    #model_comparison = finding_best_model(transformed_data)
    #model_comparison.Model()
    
    model = Model_Creation(transformed_data)
    model.execute()

if __name__ == '__main__':
    main()

    ##used from Chatgpt

    """
    models to research
    Quantile Regression (via LightGBM or GradientBoostingRegressor)
    """