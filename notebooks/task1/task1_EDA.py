import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load datasets
income_file_path = "cleaned_Income.csv"
jobs_file_path = "cleaned_Jobs.csv"
people_file_path = "cleaned_People.csv"

income_df = pd.read_csv(income_file_path)
jobs_df = pd.read_csv(jobs_file_path)
people_df = pd.read_csv(people_file_path)

# Pivot and merge datasets
income_pivoted = income_df.pivot(index=["FIPS", "State", "County"], columns="Attribute", values="Value").reset_index()
jobs_pivoted = jobs_df.pivot(index=["FIPS", "State", "County"], columns="Attribute", values="Value").reset_index()
people_pivoted = people_df.pivot(index=["FIPS", "State", "County"], columns="Attribute", values="Value").reset_index()

merged_df = pd.merge(income_pivoted, jobs_pivoted, on=["FIPS", "State", "County"], how="outer")
merged_df = pd.merge(merged_df, people_pivoted, on=["FIPS", "State", "County"], how="outer")

# Fill missing values with 0
merged_df.fillna(0, inplace=True)

# List of key numerical columns for analysis
numerical_columns = ['Median_HH_Inc_ACS', 'ForeignBornPct', 'ForeignBornNum', 'NumCivEmployed']

# 1. Histograms for Quantitative Data
for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    data = merged_df[column].dropna()
    # Apply log transformation for skewed data
    if column in ['ForeignBornNum', 'NumCivEmployed']:
        data = np.log1p(data)
        plt.title(f'Log-Transformed Histogram of {column}')
        plt.xlabel(f'Log of {column}')
    else:
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
    sns.histplot(data, kde=True)
    plt.ylabel('Frequency')
    plt.show()

# 2. Bar Plots for Categorical Data
# Bar plot for 'State' (Top 10 states by frequency)
plt.figure(figsize=(12, 6))
top_states = merged_df['State'].value_counts().head(10).index
sns.countplot(data=merged_df[merged_df['State'].isin(top_states)], x='State', order=top_states)
plt.title('Bar Plot of Top 10 States')
plt.xlabel('State')
plt.ylabel('Count')
plt.show()

# Bar plot for 'ForeignBornPct_Binned'
if 'ForeignBornPct_Binned' in merged_df.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=merged_df, x='ForeignBornPct_Binned')
    plt.title('Bar Plot of ForeignBornPct Binned')
    plt.xlabel('Foreign Born Percentage Category')
    plt.ylabel('Count')
    plt.show()

# 3. Box Plots for Numerical Data
for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    data = merged_df[column].dropna()
    if column in ['ForeignBornNum', 'NumCivEmployed']:
        data = np.log1p(data)
        plt.title(f'Log-Transformed Box Plot of {column}')
        plt.xlabel(f'Log of {column}')
    else:
        plt.title(f'Box Plot of {column}')
        plt.xlabel(column)
    sns.boxplot(x=data)
    plt.show()

# 4. Summary Statistics for Key Variables
summary_statistics = merged_df[numerical_columns].describe()
print("\nSummary Statistics for Key Numerical Variables:")
print(summary_statistics)

# 5. Correlation Heatmap for Numerical Variables
plt.figure(figsize=(8, 6))
corr_matrix = merged_df[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Key Numerical Variables')
plt.show()
