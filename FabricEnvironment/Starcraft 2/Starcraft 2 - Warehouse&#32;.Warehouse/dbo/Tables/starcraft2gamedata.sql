CREATE TABLE [dbo].[starcraft2gamedata] (

	[game_id] bigint NULL, 
	[start_time] datetime2(6) NULL, 
	[end_time] datetime2(6) NULL, 
	[map] varchar(8000) NULL, 
	[player1_name] varchar(8000) NULL, 
	[player1_faction] varchar(8000) NULL, 
	[player1_actionCount] bigint NULL, 
	[player2_name] varchar(8000) NULL, 
	[player2_faction] varchar(8000) NULL, 
	[player2_actionCount] bigint NULL, 
	[winner_name] varchar(8000) NULL, 
	[game_duration_minutes] float NULL, 
	[winner_faction] varchar(8000) NULL, 
	[player1_apm] bigint NULL, 
	[player2_apm] bigint NULL
);