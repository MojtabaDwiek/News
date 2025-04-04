import pandas as pd\

df = pd.read_csv('bbc_news.csv')

#print(df)

#Display first 5 rows of the dataset
#print(df.head())

#Display last 5 rows of the dataframe
#print(df.tail())

#display dataset info
#print(df.info())

#print the summary statistics of the dataframe
#print(df.describe())

#print how many null values are in the data frame
#print(df.isnull().sum())

#numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
#categorical_cols = df.select_dtypes(include=['object']).columns
#print("Numerical columns : " ,numerical_cols)
#print("Categorical columns : " ,categorical_cols)

#drop missing values
#df=df.dropna(axis=0) #drop rows with missing values
#df=df.dropna(axis=1) #drop columns with missing values