import pandas

#A DataFrame is a 2-D table of data (rows and columns) inside Python, designed for data analysis.

def load_data(file):
    raw_data = pandas.read_csv(file) #now this returns a data frame 
    return raw_data

