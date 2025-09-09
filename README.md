# Fabric Copilot Demo
Welcome to the Fabric Copilot Demo repository. This repository contains briefing presentations, sample Fabric items and datasets, as well as step-by-step prompt guides to demonstrate Copilot's capabilities in each different workload. 

## Available Demos
Each different dataset allows you to demo one or more workloads. Please click on each demo in the list to learn more.

1. [Starcraft 2 - Data Pipeline, Dataflows, Data Warehouse, Notebooks](/Demos/Starcraft_2.md)
2. [Stock Market - KQL Queryset, Real Time Dashboard](/Demos/Stock_Market.md)
3. [Regional Sales Sample - Power BI](Demos/Regional_Sales.md)
4. [Heart Failure - End to End Data Science]()

## Installation Instructions
This repository contains all required Fabric artifacts and data. Follow these instructions to set up your demo in your own Fabric environment.

*Before you start these installation steps, fork this repository. If you don't fork this repository you won't be able to create the correct credentials that Fabric needs to connect and import the items.*

### 1 - Prerequisites
- You must have access to a Fabric Capacity and blank Workspace on which you have Admin permissions.
- The GitHub integration settings must be turned on: [Learn more](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=azure-devops%2CAzure%2Ccommit-to-git#fabric-prerequisites)

### 2 - Connect to your forked repository
Follow [these instructions](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=github%2CAzure%2Ccommit-to-git#git-prerequisites) to connect to your repository. The last step needed is **Connect and sync**.

### 3 - Run the setup notebook
The GitHub integration brings all the Fabric items into your workspace, but you still have to import the data. The notebook titled `Data Setup` contains code and instructions that will allow you to populate the Fabric items with the necessary data. You may run the whole notebook if you will use all demos or select only the cells that interest you.
