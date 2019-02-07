'''
Created on Jan 24, 2019

@author: sthapa
'''


#print(os.getcwd());


import os
import pandas as pd
import numpy as np
import matplotlib as mlt
from nt import getcwd




df_csv = pd.read_csv("IRIS.csv", sep = ',')
df_excel = pd.read_excel("kuiper.xls", sep = ',')
#print(df_csv.columns)
#print(df_excel.columns)
#print(os.getcwd());
#print(type(df_excel))
#print(df_excel.shape)

#print(df_excel.head(3))

#print(df_excel.tail(4))

#print(df_csv)
#getting first 10 rows of the data set
#print(df_excel.iloc[:10,:4])
#select first 4 columns
#print(df_excel.iloc[:,:4])

#unique values in a column

#print(df_excel['Model'].unique())

#count if the unique values in a column
#print(df_excel['Model'].nunique())

#distribution of unique values in a column

#print(df_excel['Model'].value_counts())
"""
df = 25
df1 = "i love india"
"""



#mean median variance std

#print(df_excel['Model'].mean())
#summary

#print(df_excel['Model'].describe())

#writing to a file

#df_csv.to_csv("df_excel_practise.csv", index = False)

os.chdir("C:\Analytics\Edwisor")
#print(os.getcwd())

#create array
#print(np.arange(10))

#create list

ls = ["india",23,45,67]

sample_matrix = np.matrix('1 2 3;3 4 5')

#print(np.transpose(sample_matrix))

df = pd.DataFrame({'age':[1,2,44,9],'Gender':["M","F","F","M"],'Income': [5,6,7,3]})

#print(df)
#renaming
df = df.rename(columns = {'Gender':'gender_v1' , 'Income':'Income_v1'})
#print(df)


from ggplot import mtcars
df_mtcars = mtcars
df_mtcars_subset = df_mtcars[['hp', 'cyl' , 'carb']]











