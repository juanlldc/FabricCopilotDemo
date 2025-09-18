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

# MARKDOWN ********************

# Run the following cell if you will be using the Heart Failure demo. The code will ingest the necessary file, load it into the lakehouse and transform it into a delta table.

# CELL ********************

import urllib.request
import os

# Define the URL and download location
csv_url = "https://raw.githubusercontent.com/juanlldc/FabricCopilotDemo/ba1b794e7349c8a1fc74e6e591659963ae998edc/Data/heartdata.csv"
download_path = "/lakehouse/default/Files/heartdata.csv"

# Download the CSV from the URL
urllib.request.urlretrieve(csv_url, download_path)

# Confirm file was downloaded
print("Downloaded CSV to:", download_path)

df = spark.read.format("csv").option("header","true").load("Files/heartdata.csv")
# df now is a Spark DataFrame containing CSV data from "Files/heartdata.csv".
display(df)

# Save the DataFrame 'df' to the lakehouse as a table named 'heartdata'
df.write.format("delta").mode("overwrite").saveAsTable("heartdata")

import os

csv_path = "/lakehouse/default/Files/heartdata.csv"

if os.path.exists(csv_path):
    os.remove(csv_path)
    print(f"Deleted: {csv_path}")
else:
    print(f"File not found: {csv_path}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
