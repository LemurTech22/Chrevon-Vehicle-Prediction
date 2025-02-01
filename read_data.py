import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_name):
    data = pd.read_csv(file_name)
    return data

def plot_data(data):
    data.plot()

def main():
    print(read_data('training.csv'))
    plot_data(read_data('training.csv'))
    plt.show()

if __name__ == '__main__':
    main()
