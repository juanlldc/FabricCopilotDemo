# Introduction
This demo covers Power BI CoPilot and all its features. We look at a generic Regional Sales report that shows data for a sales group. To hihglight the usefullness of CoPilot we look at this report as though we have never seen it before, to show how CoPilot can assist with development and analysis.

## Fabric Resources
In your Fabric Workspace, browse to the Heart Regional Sales folder. The following Fabric resources are available for this demo:
- Regional Sales Sample - Report that we will be using for bulk of demo. Will also need to download this .pbix to the desktop to demonstrate those features.
- Regional Sales Sample (POST AI Prep) - this is the sames as the previous report but has the Prep Data for AI steps completed to demonstrate with the Standalone CoPilot.


## Tips

- This document walks the user through delivering this Fabric and PBI CoPilot demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.

# Regional Sales Sample (Power BI)
## Prep
Ensure you have the `Regional Sales Sample` report in the workspace. When you get to the Standalone CoPilot section, you need to make sure the Prep Data for AI version of the report has been uploaded.

## Report Viewer
1. In this section we are showing what CoPilot can do for Reprot Viewers. This works in: reports, apps, and embedded. The main reason for adoption of this is to increase the value of business users in working with the data. Instead of having to request new reports to get answers to questions they can just chat with CoPilot and get answers that way. It also cites all sources, so business users can be confident in their assessments. Lay out these value propositions before going through the demo prompts.
2. Highlight that this demo is using a report you have never seen before, and all the analysis you are gaining is accomplished very easily with CoPilot.
1. Help function, ask CoPilot what it can do
    - `What functions can you perform? Give me a summary of what you can do`
2. Ask questions about the data
    - `Which industry had the most revenue won in June 2020?`
3. Understand the report
    - `What is this report page about? Give me a concise summary of content`
    - `Identify the top insights or unusual events and show them in a bulleted list. Use one short sentence for each item`
    - `Is there anything critical I should follow up on in this report? Keep your response concise`
4. Summarize
    - `Give me an executive summary of this report. Be concise. Use a bulleted list`
    - `Summarize the Forecast by Location visual`
    - `Summarize underlying semantic model`

## Report Editor (Web)
1. This section shows how CoPilot can be used to help report builders. It can create some pre-canned reports but it is limited in that it can only create whole pages, that follow a pretty general formula for layout and content.
1. Select the generated response in the CoPilot pane, `Suggest content`.
2. From the list of suggested content select one to `Create report page`.
3. From the visual list, add the `Narrative` visual. Give it a prompt `Summarize this report page` and add it to the report.
    - The upside of this visual is that as the data changes, so does the information in the Narrative visual. No longer do we need to use text boxes that have to manualy be updated to inlcude meta information about the reports or the model, we can give that prompt to CoPilot.

## Report Editor (Desktop)
1. Continuation of the report editior features, but these are only avaliable on desktop.
1. DAX Queries
    - On the `DAX query view` tab on the left, select the CoPilot button in the top pane. Ask CoPilot to `Suggest measures`, then select `Keep query`.
2. Add descriptions for semantic model measures.
    - In the `Model view` tab on the left, select the measures group on the right hand side and select one of the measures. With it selected, click on the `Create with CoPilot (preview)` button under the description to add an automatic description.

## Prep Data for AI
1. Here we show what needs to be done to get data ready for the Standalon CoPilot. it includes 5 sections:
    - AI Data Schema - we can select which tables/columns will be used in analysis by CoPilot
    - Verified Answers - we can setup sepcific visuals to return to get answers that are known by the business and have a verified answer that we want to return.
    - AI Instructions - we can give CoPilot specific instructions for each semantic model it connects to, like with other LLMs to customize it.
    - Optimize the Data Model - we don't go over this in the demo, but mention it here. It is always good practice to have an optimized and efficient data model conforming to best practices, but for AI especially CoPilot can return better answers faster if the data model is optmized.
    - Descriptions for Measures - this helps CoPilot get more accurate answers. We showed this in the previous part of how CoPilot can create these descriptions for us.
1. AI Data Schema
    - In the `Report view` tab on the left hand side, select the `Prep data for AI` in the top pane.
    - Under the `Simplify the data schema` select a subset of the tables to be used by the CoPilot.
2. Verified Answers
    - Select the `Revenue Won and Revenue in Pipeline by Product LOB` on the PBI report page and click the elipses on the top right of the visual and select the `Set up a verified answer`.
    - Select the three CoPilot suggestions for the phrases connected to this verified answer.
3. AI Instructions
    - In the AI instructions tab add any instructions on the personality or information the CoPilot should use when accessing this report.
    - Example: `If asked whether something is "on target", show Total Sales for the current Month.`

## Standalone CoPilot
1. This is the standalone CoPilot that sits on the entire Fabric OneLake. You can search anything across all capacities. It is also doing more than simple keyword search, it is actually looking at the contents of the reports and data models to determine best fit for the search.
1. Find items in Power BI
    - `Find reports that will show me lost opportunities` This should bring up the `Regional Sales Sample`.
2. We can also show the difference here between a model that has been prepped for AI and one that hasn't.
2. Attaching the AI prepped report, then ask `What opportunities by industry made the most money?`
3. Attaching the AI prepped report, then ask `Product line revenue?` This should bring up the verified answer.

4. Attack the NON prepped for AI report and ask any question. It will give an answer but also a warning saying the answers are not prepped for AI and may be unreliable.
