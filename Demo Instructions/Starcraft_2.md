This document walks the user through delivering this Fabric and PBI CoPilot demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.

# Starcraft 2 (Data Pipeline, Dataflows, Data Warehouse, Notebooks)
## Prep 
Create a ADLS2 instance with the `starcraft2_fake_dataset_updated.csv` to load using the data pipeline

## Data Pipelines
1. `get data using copy data activity`
2. Give connection info using the `/` command in the CoPilot pane
3. Add Teams message notification on success. (This should fail, so add it but do not finish setting it up, this is to demonstrate errors.)
4. `summarize this pipeline`
    - Click on the `Update descriptions` option that it responds with to change the item and pipeline descriptions.
5. `run this pipeline`
6. Once the pipeline runs, the Teams1 activity should fail, in the run window, select the CoPilot icon next to the failed run to get an explanation of the error.

## Dataflows Gen 2
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
1. Load data
    - `load starcraft2gamedata into a dataFrame`
2. Transformation
    - `for the dataframe perform transformations to clean up the data for a silver layer lakehouse. include new columns called duration that is the duration between start_time and end_time, a new column called winner_faction that is the faction of the winner player, and include columns for each player called apm that takes the action count and divides it by the duration of the game`
3. Write back to Lakehouse
    - `write this dataframe back to the Lakehouse001 in a new table called silver_starcraft2gamedata`
4. Experiment
    - This prompt will often create an experiment to make a model to predict winners.
    - `using the dataframe, create an experiment that uses this data to determine the winner of a game`
