# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0063a8bd-4220-414e-ab28-7fefbad4d096",
# META       "default_lakehouse_name": "Lakehouse",
# META       "default_lakehouse_workspace_id": "12c07eee-3014-4be9-8d52-15dbc8c8bedd",
# META       "known_lakehouses": [
# META         {
# META           "id": "0063a8bd-4220-414e-ab28-7fefbad4d096"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Load the starcraft2gamedata table into a Spark DataFrame
spark_df = spark.read.table("starcraft2gamedata")

# Initialize max_rows_to_read to a reasonable limit for larger tables.
max_rows_to_read = 1000
spark_df = spark_df.limit(max_rows_to_read)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#### ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Convert start_time and end_time to timestamp data types
from pyspark.sql.functions import col, unix_timestamp

spark_df = spark_df.withColumn("start_time", unix_timestamp(col("start_time")))
spark_df = spark_df.withColumn("end_time", unix_timestamp(col("end_time")))

# Calculate duration (in minutes)
from pyspark.sql.functions import (col,expr, when)

spark_df = spark_df.withColumn("duration", (col("end_time") - col("start_time")) / 60)

# Create winner_faction column
spark_df = spark_df.withColumn("winner_faction", 
                when(col("winner_name") == col("player1_name"), col("player1_faction"))
                .otherwise(col("player2_faction")))

# Calculate APM (Actions Per Minute) for each player
spark_df = spark_df.withColumn("player1_apm", col("player1_actionCount") / col("duration"))
spark_df = spark_df.withColumn("player2_apm", col("player2_actionCount") / col("duration"))

spark_df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************


# CELL ********************

# ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.
# Save the transformed DataFrame to Lakehouse001 in a new table called silver_starcraft2gamedata
spark_df.write.mode("overwrite").format("delta").saveAsTable("silver_starcraft2gamedata")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import when, col, avg, count
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Calculate win rate for each faction
win_rate_faction = spark_df.groupBy("winner_faction").agg(count('*').alias('win_count'))
total_games_faction = spark_df.select("player1_faction").union(spark_df.select("player2_faction"))\
                             .groupBy("player1_faction").agg(count('*').alias('game_count')).withColumnRenamed("player1_faction", "faction")
win_rate_faction = win_rate_faction.join(total_games_faction, win_rate_faction.winner_faction == total_games_faction.faction)\
                                   .select(col("winner_faction"), (col("win_count") / col("game_count")).alias("win_rate"))

# Calculate average APM of winners
winners_df = spark_df.where(col("winner_name") == col("player1_name"))\
                     .select(col("player1_apm").alias("winner_apm"), col("player1_faction").alias("winner_faction"))\
                     .union(spark_df.where(col("winner_name") == col("player2_name"))\
                                     .select(col("player2_apm").alias("winner_apm"), col("player2_faction").alias("winner_faction")))
avg_apm_winners = winners_df.groupBy("winner_faction").agg(avg("winner_apm").alias("avg_apm"))

# Combine data to prepare for analysis
combined_data = win_rate_faction.join(avg_apm_winners, win_rate_faction.winner_faction == avg_apm_winners.winner_faction)\
                                .select(win_rate_faction.winner_faction, "win_rate", "avg_apm")

# Using logistic regression to evaluate predictive power of faction and apm
# Prepare dataset for logistic regression
data = spark_df.withColumn('winner', when(col('winner_name') == col('player1_name'), 1).otherwise(0))
vector_assembler = VectorAssembler(inputCols=["player1_apm", "player2_apm"], outputCol="features")
data = vector_assembler.transform(data)

# Apply logistic regression
lr = LogisticRegression(labelCol="winner", featuresCol="features")
lr_model = lr.fit(data)
predictions = lr_model.transform(data)

# Evaluate model
evaluator = BinaryClassificationEvaluator(labelCol="winner")
accuracy = evaluator.evaluate(predictions)

print(f"Model accuracy: {accuracy}")

combined_data.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Inspect the schema
spark_df.printSchema()

# Show first few rows
spark_df.show(5)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Summary statistics for all columns
spark_df.describe().show()

# Count nulls per column
from pyspark.sql.functions import col, sum as spark_sum
spark_df.select([spark_sum(col(c).isNull().cast("int")).alias(c) for c in spark_df.columns]).show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Calculate win rates by faction
faction_win_rates = spark_df.groupBy('winner_faction').agg({'winner_faction': 'count'}).toPandas()

# In Pandas:
import matplotlib.pyplot as plt

# Rename the column for better readability
faction_win_rates = faction_win_rates.rename(columns={'count(winner_faction)': 'win_rate'})

# Plotting the bar chart
faction_win_rates.plot.bar(x='winner_faction', y='win_rate')
plt.title('Win Rate by Faction')
plt.ylabel('Win Rate')
plt.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
