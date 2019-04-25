if __name__ == '__main__':
    import pymongo
    import pandas as pd
    import numpy as np
    import os
    import datetime
    import sys 
    import csv
    from sklearn import svm


    filename = "data.csv"
    
    df = pd.read_csv(filename)