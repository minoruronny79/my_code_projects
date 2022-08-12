from distutils.log import error
import pandas as pd
import numpy as np
import pytest
import logging
import os

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    #format='%(name)s - %(levelname)s - %(message)s' 
)

def read_data(file_path):
    try:
        df=pd.read_csv(file_path)
        logging.info("SUCCESs: The shape is {}: ".format(df.shape))
        logging.info('SUCCESS: Data was retrieved')
        return df
    except FileNotFoundError:
        logging.error("ERROR: There is no file")

df=read_data("F:/PythonTraining/Udacity")
#print(df.shape)
print(type(df))
print(os.getcwd())