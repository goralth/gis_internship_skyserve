import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the uploaded CSV file to examine its structure and contents

data = pd.read_csv("D:\\DataFilesPython\\MainFlow Dataset\\USvideos.csv")

# Display the first few rows and summary information about the dataset
data.head()
data.info()


# Select numeric columns for analysis
numeric_columns = ['category_id', 'views', 'likes', 'dislikes', 'comment_count']

# 1. Distribution of each numeric variable
for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(data[column], kde=True, bins=30, color='blue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# 2. Boxplots for identifying outliers
for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=data[column], color='orange')
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.show()

   # 3. Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = data[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show() 

