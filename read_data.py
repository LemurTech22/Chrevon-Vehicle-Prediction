import numpy as np
import pandas as pd

def read_data():
    data = pd.read_csv('training.csv')
    return data

def main():
    print(read_data())

if __name__ == '__main__':
    main()
