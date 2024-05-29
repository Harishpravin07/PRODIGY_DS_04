import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset with manual column names
file_path = 'twitter_training.csv'
column_names = ['ID', 'Entity', 'Sentiment', 'Text']

try:
    df = pd.read_csv(file_path, names=column_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the columns to verify
print("Columns in the dataset:")
print(df.columns)

# Display the first few rows of the dataframe to inspect data
print("First few rows of the dataset:")
print(df.head())

# Identify the correct sentiment column
sentiment_column = 'Sentiment'

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Display the sentiment distribution
print("\nSentiment distribution:")
print(df[sentiment_column].value_counts())

# Plot the sentiment distribution
plt.figure(figsize=(10, 6))
sns.countplot(x=sentiment_column, data=df, palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
