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




#summary:


#Data Exploration:

#df.head()  # First 5 rows
#df.tail()  # Last 5 rows
#df.sample(5)  # Random 5 rows
#df.shape  # (rows, columns)
#df.columns  # Column names
#df.info()  # Data types and memory usage
#df.describe()  # Summary statistics
#df.nunique()  # Unique values per column
#df.isnull().sum()  # Count of nulls per column
#df['column'].value_counts()  # Frequency counts
#df.corr()  # Correlation matrix
#df.memory_usage()  # Memory usage per column



#Data Selection:

#df['column']  # Single column
#df[['col1', 'col2']]  # Multiple columns
#df.loc[row_indexer, column_indexer]  # Label-based selection
#df.iloc[row_position, column_position]  # Position-based selection
#df.query('column > value')  # Query method
#df.filter(items=['col1', 'col2'])  # Filter columns
#df.filter(like='text')  # Columns containing text
#df.filter(regex='regex_pattern')  # Regex column selection
#df.xs('index_value')  # Cross-section
#df.where(df > 0)  # Where condition
#df.at[index, 'column']  # Single value by label
#df.iat[row, col]  # Single value by position


#Data Cleaning:

#df.dropna()  # Drop rows with NA
#df.dropna(axis=1)  # Drop columns with NA
#df.fillna(value)  # Fill NA with value
#df.fillna(method='ffill')  # Forward fill
#df.replace(old_val, new_val)  # Replace values
#df.rename(columns={'old':'new'})  # Rename columns
#df.rename(index={'old':'new'})  # Rename index
#df.drop_duplicates()  # Remove duplicates
#df.drop(['col1', 'col2'], axis=1)  # Drop columns
#df.astype('int')  # Change data type
#pd.to_numeric(df['column'])  # Convert to numeric
#pd.to_datetime(df['date_column'])  # Convert to datetime
#df.reset_index()  # Reset index
#df.set_index('column')  # Set new index


#Data Transformation:

#df.sort_values('column')  # Sort by column
#df.sort_index()  # Sort by index
#df.rank()  # Rank values
#df.pivot_table(values='A', index='B', columns='C')  # Pivot table
#df.melt(id_vars=['col1'], value_vars=['col2', 'col3'])  # Unpivot
#df.groupby('column').mean()  # Group by and aggregate
#df.groupby(['col1', 'col2']).agg({'col3':'sum', 'col4':'mean'})  # Multiple aggregations
#df.pivot(index='A', columns='B', values='C')  # Pivot
#pd.crosstab(df['col1'], df['col2'])  # Cross-tabulation
#df.apply(lambda x: x*2)  # Apply function
#df.applymap(lambda x: len(str(x)))  # Element-wise function
#df['new_col'] = df['col1'] + df['col2']  # Create new column
#df.assign(new_col = df['col1'] * 10)  # Assign new column
#df.eval('new_col = col1 + col2')  # Evaluate expression


#Visualization:

#df.plot()  # Basic plot
#df.plot.line()  # Line plot
#df.plot.bar()  # Bar plot
#df.plot.barh()  # Horizontal bar plot
#df.plot.hist()  # Histogram
#df.plot.box()  # Box plot
#df.plot.kde()  # Kernel Density Estimate
#df.plot.density()  # Density plot
#df.plot.area()  # Area plot
#df.plot.scatter(x='col1', y='col2')  # Scatter plot
#df.plot.hexbin(x='col1', y='col2')  # Hexbin plot
#df.plot.pie(y='column')  # Pie chart