import pandas as pd
import numpy as np

def readCsv(filePath):
    return pd.read_csv(filePath, encoding='euc-kr')

def getHeader(df):
    return df.columns

def getValues(df):
    return df.to_numpy().tolist()