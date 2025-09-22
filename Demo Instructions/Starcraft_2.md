# Introduction
This demo covers Fabric CoPilot features in four different items:
- Data Pipeline
- Dataflow Gen 2
- Data Warehouse
- Notebooks

The goal of this demo is to demonstrate how CoPilot can help a typical development cycle of ingesting data, transforming it and getting quick analysis done. The demo dataset is faked data from a Starcraft 2 tournament in August. The main theme of this demo it to try to analyze whether your win rate is best determined by the faction you play or the Action Per Minute (APM) you are able to do.

## Fabric Resources
In your Fabric Workspace, browse to the Regional Sales folder. The following Fabric resources are available for this demo:
- DataPipeline001 - This is what will ingest the data from ADLS2 into Fabric.
- Lakehouse001 - where data is stored from the data copy pipeline as well as the silver transformed data from the Notebooks. This is the same Lakehouse that also stores the data for the Heart Failure demo.
- Dataflow001 - transformation dataflow to take the data from the lakehouse to the data warehouse.
- Warehouse001 - gold layer of the demo and where the final analysis will be completed.
- Notebook001 - takes in data from the lakehouse and performs the data transformations, writes it back out to the lakehouse in a silver table, and creates an experiment to best determine winner.


## Tips

- This document walks the user through delivering this Fabric demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.
- This demo gives a very brief overview of the Notebooks CoPilot. For a comprehensive looks at what it can do, check out the Heart Failure Data Engineering demo we also have here.

# Starcraft 2 (Data Pipeline, Dataflows, Data Warehouse, Notebooks)
## Prep 
Create a ADLS2 instance with the `starcraft2_fake_dataset_updated.csv` to load using the data pipeline. It is advised to create a workspace identity to connect to the ADLS2 instance.
- [Creating a Fabric Workspace Identity](https://learn.microsoft.com/en-us/fabric/security/workspace-identity)
- [Using Fabric Workspace Identity to connect to ADLS](https://learn.microsoft.com/en-us/fabric/security/workspace-identity-authenticate)

If ADLS is not avaliable to you, upload the fake Starcraft 2 dataset directly to the Lakehouse. You can then skip the Data Pipelines demo and move right to the Dataflows.

## Data Pipelines
1. Open up CoPilot in the top right
1. `get data using copy data activity`
2. Give connection info using the `/` command in the CoPilot pane
3. Add Teams message notification on success. (This should fail, so add it but do not finish setting it up, this is to demonstrate errors.)
4. `summarize this pipeline`
    - Click on the `Update descriptions` option that it responds with to change the item and pipeline descriptions.
5. `run this pipeline`
6. Once the pipeline runs, the Teams1 activity should fail, in the run window, select the CoPilot icon next to the failed run to get an explanation of the error.
    - This lets us demonstrate the error handling of CoPilot. The Teams activity should not work but allow you to run the pipeline. If it doesn't let you run pipeline you can put in any activity and give it bad information so that it will fail.

## Dataflows Gen 2
1. Goal here is to transform the data so we can perform our analysis. We need several transformations to accomplish our end goals:
    - Get the Actions Per Minute (APM) - this will require knowing the duration of the game in minutes
    - Get the winning Faction - extract which faction won each round
1. Connect to the data source
    - `get data from the Lakehouse001`
2. Convert columns
    - `convert game_id, player1_actioncount, player2_actioncount to integer types, and convert start_time and end_time into datetime`
3. Make new column for game duration
    - `make a new column called game_duration_minutes that is the time between start_time and end_time, make it type decimal`
4. Make new colum for winner faction
    - `make a new column called winner_faction that is the winner_name match to player1_name or player2_name referencing the player1_faction or player2_faction`
5. Make new column for Player 1 APM
    - `create a new column called player1_apm that takes player1_actioncount divided by the game_duration_minutes, round to whole number`
6. Make new column for Player 2 APM
    - `create a new column called player2_apm that takes player2_actioncount divided by the game_duration_minutes, round to whole number`
7. Summary (Can right click the query on left hand side pane and select `Explain this Query`)
    - `provide a summary of this query and applied steps`

## Data Warehouse
1. Typically warehousing is used for creating robust gold models, but here we are going to use CoPilots ability to generate SQL to provide us with some quick insights. We can show here that we don't need to make reports to get answers to questions.
1. Get intelligent insights
    - `provide some intelligent insights`
    - This can return some recommended queries to run, like faction and APM win rate. You can click on these to develop the rest of the queries.
2. Faction win rate sumamry
    - `provide a summary of the factions and their win rates`
3. Player win rate based on APM
    - `get the win rates of all the players and their average apm`
4. Mess up one of the SQL statements, then run the query which fails then you can select the `Fix query errors` in the top pane.
5. You can start typing to get CoPilot to suggest code segments.

## Notebooks
1. The goal here is to show we can also use Notebooks and Spark engines to perform transformations, as well as experiments. This section is strictly not neccesary, but if the audience is more Spark based they will find this more useful than the Dataflows.
1. Start the Spark Session
2. Open the CoPilot pane
1. Load data
    - `load starcraft2gamedata into a dataFrame`
    - For each code block returned you will have to manually copy it over to a cell.
2. Transformation
    - `for the dataframe perform transformations to clean up the data for a silver layer lakehouse. include new columns called duration that is the duration between start_time and end_time, a new column called winner_faction that is the faction of the winner player, and include columns for each player called apm that takes the action count and divides it by the duration of the game`
3. Write back to Lakehouse
    - `write this dataframe back to the Lakehouse001 in a new table called silver_starcraft2gamedata`
4. Experiment
    - This prompt will often create an experiment to make a model to predict winners.
    - `using the dataframe, create an experiment that uses this data to determine the winner of a game`
