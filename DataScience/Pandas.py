import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

book_title=['C++','Java','Python','Javascript']
# print(pd.Series(book_title))
book_title=pd.Series(book_title)
book_title.index=['a','b','c','d']
print(book_title['c'])

# dataframe
arr=np.random.randint(10,100,size=(6,4))
df=pd.DataFrame(data=arr)
# print(df)
# extracting data column
df[2]
# changing column names
df.columns=['A','B','C','D']
# print(df)
# print(df.shape)
# first 3 rows
df.head(n=3)
# last 3 rows 
df.tail(n=3)
# extracting multiple columns
cols=['A','B']
df[cols] 
# specify the order
df[['B','D','A']]
# add new columns 
df['A+B']=df['A']+df['B']
# print(df)
# drop column 
df=df.drop(columns=['A+B'])
#  df.drop(columns=['A+B'],implace=True)
# print(df)
df.index="p q r s t u".split()
# print(df)

# extracting rows  
# print(df.loc['p'])
# iloc-getting row by number 
df.iloc[4]

# multiple rows 
# for getting row 2 to 4
df.iloc[2:5]
# for getting row 2 to 4 and column A to B
df.iloc[2:5][['A','B']]
# for getting last two rows and last two columns
df.iloc[-2:,-2:]

# masking 
mask=df>30
# print(df[mask])

# extract all thos rows whose value at column 'B' is > 40
mask=df['B']>40
# print(mask)
# print(df[mask])

# extract column 'C' and 'D' where column 'B' has value is > 40
# print(df[df['B']>40][['C','D']])


# conditions
(df['A']>40) & (df['D']<50)
# print(df[(df['A'] > 40) & (df['D'] < 50)])

# converting to numpy 
df_array=df.values

# shows first five rows
# print(df.head())

# Iris dataset
iris=pd.read_csv("./iris.csv")
type(iris)
# print(iris.head())

# print(iris.shape)
# print(iris.columns)

# print(iris.dtypes)
# print(iris.info())


# print(iris.describe())

# print(iris['species'])

# print(iris['species'].nunique())
# print(iris['species'].unique())

# How many setosa flowers are there
# print(iris[iris['species'] == 'setosa'])
# print(iris[iris['species'] == 'setosa'].shape)
# anther method
iris['species'].value_counts()['virginica']

iris['sepal_length'].mean()
iris['petal_length'].max()

iris['petal_width'].sum()

# print(iris.sort_values(by=['sepal_length','sepal_width']))

# applying a function to a column
# print(iris['species'].apply(len))

# values will get added to itself
iris.apply(lambda x:x+x)

# grouping data together
# print(iris)
# print(iris.aggregate('min'))

# print(iris.aggregate(['max','min','median','mean']))

# group by
groupby=iris.groupby('species')   
print(groupby)

# print(groupby.min())
groupby.count()
# print(groupby.mean())

# print(iris[iris['species']=='setosa']['sepal_length'].mean())

groupby.describe()
groupby.describe().T

# dealing with missing values
nan_idx=np.random.randint(0,150,20)
# print(nan_idx)
iris['sepal_length'][nan_idx] =np.nan
# print(iris['sepal_length'])

nan_idx = np.random.randint(0, 150, 15)
iris['petal_width'][nan_idx] = np.nan
# print(iris['sepal_length'])

# print(iris.isna().sum())

# deleting the rows having na values
# iris=iris.dropna()
# print(iris)

iris['sepal_length']=iris['sepal_length'].fillna(value=round(iris['sepal_length'].mean(),1))
iris['petal_width'] = iris['petal_width'].fillna(value=round(iris['petal_width'].mean(), 1))
# print(iris)


# Edit/Concat dataframes
new_df=pd.DataFrame(np.random.randint(0,7,size=(10,4)))
# print(new_df)

new_df['species']='new-species'
new_df.columns=iris.columns

# print(new_df.head())

iris=pd.concat((iris,new_df),axis=0)
print(iris)
# axis = 0, concat by row
# axis = 1, concat by column

