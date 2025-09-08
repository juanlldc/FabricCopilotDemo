Load heartdata as a dataframe called heart

Tell me more about the heart dataset. Explain in plain text, do not create any code. 

Show me a histogram for the distribution of age

What more data exploration and visualization can I do?

Analyze what empty values are present in the dataframe

%%chat
Explain in plain text what the different options to drop missing values are. Do not create any code. 

%%code
Drop all rows with any missing values

/explain, /add_comments, /fix and then /optimize

data_df1 = cleaned_spark_df
obj = data_df1select_dtypes(include='object')
not_obj = data_df1.select_dtypes(exclude='object')
for i in range(0, obj.shape[1]):
  obj.iloc[:,i] = lab.fit_transform(obj.iloc[:,i])
df_new = pd.concat([obj, not_obj], axis=1)
df_new.head(10)

%%chat

With df_new being our final version of the data, what machine learning models do you recommend to predict the likelyhood of heart failure? Explain in plain text, do not create any code.

Tell me more about the ROC-AUC score. What does it mean? Why is it significant? In this case, is it good or bad?
