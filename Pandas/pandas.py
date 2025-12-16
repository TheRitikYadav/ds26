import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Accessing a column
print("\nAccessing the 'Name' column:")
print(df['Name'])

# Filtering rows
print("\nFiltering rows where Age > 28:")
print(df[df['Age'] > 28])

# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# Grouping data
print("\nGrouping by 'City' and calculating average Age:")
print(df.groupby('City')['Age'].mean())