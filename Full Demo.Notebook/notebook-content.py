# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "391bac6e-2b26-4ad9-bcef-2aa736e090c2",
# META       "default_lakehouse_name": "Copilot_Demo",
# META       "default_lakehouse_workspace_id": "f22a4a9a-64c5-4932-b44a-98550784e6c7",
# META       "known_lakehouses": [
# META         {
# META           "id": "391bac6e-2b26-4ad9-bcef-2aa736e090c2"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Load the heartdata table into a DataFrame
spark_df = spark.read.table("heartdata")

# Display the DataFrame to verify it is loaded correctly
display(spark_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Display information about the DataFrame
spark_df.printSchema()
spark_df.describe().show()
spark_df.show(5)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

import plotly.express as px

# Convert the Spark DataFrame to a Pandas DataFrame for compatibility with Plotly
pandas_df = spark_df.toPandas()

# Generate the histogram
fig = px.histogram(pandas_df, x="Age", nbins=20, title="Distribution of Age", template='plotly_dark')
fig.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

fig = px.histogram(pandas_df, x="Sex", title="Count Plot of Sex", template='plotly_dark')
fig.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

fig = px.scatter(pandas_df, x="Age", y="Cholesterol", title="Age vs. Cholesterol", template='plotly_dark')
fig.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# The cell failed because the correlation matrix computation included string columns.
# We need to exclude non-numeric columns before computing the correlation matrix.

import plotly.figure_factory as ff

# Select only numeric columns for the correlation matrix
numeric_df = pandas_df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
corr_matrix = numeric_df.corr()

# Generate the heatmap
fig = ff.create_annotated_heatmap(
    z=corr_matrix.values,
    x=list(corr_matrix.columns),
    y=list(corr_matrix.index),
    annotation_text=corr_matrix.round(2).values,
    showscale=True,
    colorscale="Viridis"
)
fig.update_layout(title="Correlation Matrix Heatmap", template='plotly_dark')
fig.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Analyzing the presence of empty (null) values in the heartdata dataset

from pyspark.sql import functions as F

# Count the number of missing values in each column
missing_values = spark_df.select([F.count(F.when(F.col(column).isNull(), column)).alias(column) for column in spark_df.columns])

# Display the count of missing values for each column
missing_values.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Remove rows with any missing values

# Filter out rows with any null values
cleaned_spark_df = spark_df.dropna()

# Display the cleaned DataFrame to verify missing values are removed
cleaned_spark_df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC Drop all rows with any missing values


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Convert Spark DataFrame to Pandas DataFrame
data_df1 = cleaned_spark_df.toPandas()

# Separate object (categorical) and non-object (numerical) columns
obj = data_df1.select_dtypes(include='object')
not_obj = data_df1.select_dtypes(exclude='object')

# Initialize LabelEncoder
lab = LabelEncoder()

# Apply LabelEncoder to each categorical column
obj = obj.apply(lambda col: lab.fit_transform(col))

# Concatenate the encoded categorical columns with the numerical columns
df_new = pd.concat([obj, not_obj], axis=1)

# Display the first 10 rows of the new DataFrame
df_new.head(10)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

data_df1 = spark_df.toPandas()  # Convert Spark DataFrame to Pandas DataFrame
obj = data_df1.select_dtypes(include='object')
not_obj = data_df1.select_dtypes(exclude='object')
for i in range(0, obj.shape[1]):
  obj.iloc[:,i] = lab.fit_transform(obj.iloc[:,i])
df_new = pd.concat([obj, not_obj], axis=1)
df_new.head(10)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%chat
# MAGIC What are the steps to train a logistic regression model?

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC Generate the code for splitting the data, training the model and evaluating the model

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Convert categorical columns to numerical
from sklearn.preprocessing import LabelEncoder

# Assuming 'df_new' is your prepared DataFrame with features and target variable
X = df_new.drop(columns=['HeartDisease'])  # Features
y = df_new['HeartDisease']                # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

# Print performance metrics
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"ROC-AUC Score: {roc_auc}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
