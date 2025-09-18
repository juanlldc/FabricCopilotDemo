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

# MARKDOWN ********************

# # Heart Failure - End to End Data Science
# 
# ## Introduction
# This demo cover an end to end data science demo with the assistance of Copilot. The scenario is around building a model to predict the risk of heart failure. The initial dataset is available in the environment lakehouse in the `heartdata` table. The steps in this demo cover exploring the data, preparing it for machine learning, training a model and evaluating the results. It explores the different ways of interacting with Copilot within a notebook and the different use cases (such as brainstorming, code generation, code fixing...). 

# MARKDOWN ********************

# ### Interacting with Copilot in the Chat pane
# Try the following prompts in the Copilot Chat pane
# 1. **Code Expected** Load data - **Use the example prompt shown in the chat pane**
#    - `Load the heartdata table into a DataFrame `

# MARKDOWN ********************

# 2. **Code Expected** Analyze the dataset - **Use the example prompt shown in the chat pane**
#    - `Analyze heartdata_df and provide insights about the data`

# MARKDOWN ********************

# ### In-Cell copilot commands 
# Run each of the following commands in a new blank cell
# 
# 3.    Explain analysis results

# CELL ********************

# MAGIC %%chat
# MAGIC Based on the previous results, what can you say about the structure of heartdata_df?

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Interacting with Copilot in the Chat pane
# Try the following prompts in the Copilot Chat pane
# 
# 4. **Code Expected** Generate a visualization of interest
#    - `Show me a histogram for the distribution of age`

# MARKDOWN ********************

# 5. Further data exploration and visualization guided by Copilot
#    - `What more data exploration and visualization can I do?`
# 6. **Code Expected** Generating code from the visualizations offered
#    - **If Copilot lists a series of visualizations instead of generating a code cell, pick some from the list and ask Copilot to generate the code**

# MARKDOWN ********************

# ### In-Cell copilot commands 
# Run each of the following commands in a new blank cell
# 
# 7. Options to remediate missing values

# CELL ********************

# MAGIC %%chat
# MAGIC How can we deal with the identified missing values?

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 8. **Code Expected** Generating code to drop missing values

# CELL ********************

# MAGIC %%code
# MAGIC Drop all rows with any missing values


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Modyfing existing cells
# Click on the copilot button in the cell options. Try each of the following commands:
# 
# 9. `/explain`
#    
# 10. `/add_comments`
#     
# 11. **Code Expected**  `/fix`
#     
# 12. **Code Expected** `/optimize`

# CELL ********************

import pandas as pd
from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()
data_df1 = heartdata_df_clean.toPandas()
obj = data_df1select_dtypes(include='object')  
not_obj = data_df1.select_dtypes(exclude='object')
for i in range(0, obj.shape[1]):
  obj.iloc[:,i] = lab.fit_transform(obj.iloc[:,i])
df_ready = pd.concat([obj, not_obj], axis=1)
df_ready.head(10)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Training a Machine learning model
# Through the previous steps, Copilot helped us understand our dataset and shape the data for machine learning. Use the following prompts, either in new cells or on the chat pane, to train a model.
# 
# 13. Asking for an adequate model

# CELL ********************

# MAGIC %%chat
# MAGIC 
# MAGIC With df_ready being our final version of the data, what machine learning models do you recommend to predict the likelyhood of heart failure? Explain in plain text, do not create any code.

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 14. Asking about the steps to train a model

# CELL ********************

# MAGIC %%chat
# MAGIC What are the steps to train a logistic regression model?

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 15. **Code Expected** Training the model according to the steps (data preparation has already been done)

# CELL ********************

# MAGIC %%code
# MAGIC Generate the code for splitting the data, training the model and evaluating the model

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 16. Generating the ROC-AUC Score **Run this step if Copilot did not generate the ROC-AUC score in the previous step**

# CELL ********************

# MAGIC %%code
# MAGIC Generate the ROC-AUC score

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 17. Making sense of the scores obtained by the model 

# CELL ********************

# MAGIC %%chat
# MAGIC Tell me more about the ROC-AUC score. What does it mean? Why is it significant? In this case, is it good or bad?

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
