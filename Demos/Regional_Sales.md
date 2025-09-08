This document walks the user through delivering this Fabric and PBI CoPilot demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.

# Regional Sales Sample (Power BI)
## Prep
Ensure you have the `Regional Sales Sample` report in the workspace. When you get to the Standalone CoPilot section, you need to make sure the Prep Data for AI version of the report has been uploaded.

## Report Viewer
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
1. Select the generated response in the CoPilot pane, `Suggest content`.
2. From the list of suggested content select one to `Create report page`.
3. From the visual list, add the `Narrative` visual. Give it a prompt `Summarize this report page` and add it to the report.

## Report Editor (Desktop)
1. DAX Queries
    - On the `DAX query view` tab on the left, select the CoPilot button in the top pane. Ask CoPilot to `Suggest measures`, then select `Keep query`.
2. Add descriptions for semantic model measures.
    - In the `Model view` tab on the left, select the measures group on the right hand side and select one of the measures. With it selected, click on the `Create with CoPilot (preview)` button under the description to add an automatic description.

## Prep Data for AI
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
1. Find items in Power BI
    - `Find reports that will show me lost opportunities` This should bring up the `Regional Sales Sample`.
2. Attaching the AI prepped report, then ask `What opportunities made the most money?`
3. Attaching the AI prepped report, then ask `Product line revenue?` This should bring up the verified answer.

4. Attack the NON prepped for AI report and ask any question. It will give an answer but also a warning saying the answers are not prepped for AI and may be unreliable.
