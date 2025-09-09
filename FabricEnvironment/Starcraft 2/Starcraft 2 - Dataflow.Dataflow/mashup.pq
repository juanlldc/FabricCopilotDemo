[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "starcraft2gamedata_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "game_id", DestinationColumnName = "game_id"], [SourceColumnName = "start_time", DestinationColumnName = "start_time"], [SourceColumnName = "end_time", DestinationColumnName = "end_time"], [SourceColumnName = "map", DestinationColumnName = "map"], [SourceColumnName = "player1_name", DestinationColumnName = "player1_name"], [SourceColumnName = "player1_faction", DestinationColumnName = "player1_faction"], [SourceColumnName = "player1_actionCount", DestinationColumnName = "player1_actionCount"], [SourceColumnName = "player2_name", DestinationColumnName = "player2_name"], [SourceColumnName = "player2_faction", DestinationColumnName = "player2_faction"], [SourceColumnName = "player2_actionCount", DestinationColumnName = "player2_actionCount"], [SourceColumnName = "winner_name", DestinationColumnName = "winner_name"], [SourceColumnName = "game_duration_minutes", DestinationColumnName = "game_duration_minutes"], [SourceColumnName = "winner_faction", DestinationColumnName = "winner_faction"], [SourceColumnName = "player1_apm", DestinationColumnName = "player1_apm"], [SourceColumnName = "player2_apm", DestinationColumnName = "player2_apm"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared starcraft2gamedata = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "40c83fce-930b-4c50-b41c-3d05a8d9135b"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "07cec296-26fb-4406-99f9-9d6f8ad061b7"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "starcraft2gamedata", ItemKind = "Table"]}[Data],
  #"Remove duplicates" = Table.Distinct(#"Navigation 2", {"game_id"}),
  #"Change type" = Table.TransformColumnTypes(#"Remove duplicates", {{"game_id", Int64.Type}, {"player1_actionCount", Int64.Type}, {"player2_actionCount", Int64.Type}, {"start_time", type datetime}, {"end_time", type datetime}}),
  #"Add column" = Table.AddColumn(#"Change type", "game_duration_minutes", each Duration.TotalMinutes(
        Duration.From(
            DateTime.From([end_time]) - DateTime.From([start_time])
        )
    ), type number),
  #"Add column 1" = Table.AddColumn(#"Add column", "winner_faction", each if [winner_name] = [player1_name] then [player1_faction] else [player2_faction], type text),
  #"Add column 2" = Table.AddColumn(#"Add column 1", "player1_apm", each Number.Round([player1_actionCount] / [game_duration_minutes]), Int64.Type),
  #"Add column 3" = Table.AddColumn(#"Add column 2", "player2_apm", each Number.Round([player2_actionCount] / [game_duration_minutes]), Int64.Type)
in
  #"Add column 3";
shared starcraft2gamedata_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false]),
  Navigation_1 = Pattern{[workspaceId = "40c83fce-930b-4c50-b41c-3d05a8d9135b"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "89ea2a77-4c41-417e-a694-82c996b8d4f7"]}[Data],
  TableNavigation = Navigation_2{[Item = "starcraft2gamedata", Schema = "dbo"]}?[Data]?
in
  TableNavigation;
