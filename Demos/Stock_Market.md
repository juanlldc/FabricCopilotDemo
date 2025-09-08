This document walks the user through delivering this Fabric and PBI CoPilot demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.

# Stock Market (KQL Queryset, Real Time Dashboard)
## Prep
This data uses the `StockMarket` fake streaming data from the Eventstream. Setup the eventstream to ingest this data stream into an Eventhouse.

## KQL Queryset
*  Natural Language to KQL Examples
    - `for each stock, get the average price over the past hour`
    - `sum of all stock sales for the past 30 minutes`

## Real Time Dashboard
* Go to the `Real Time Hub` on the left hand navigation pane. Select the `StockMarket` streaming data and select the settings for it. Select the `Create Real-time Dashboard (Preview)` option. This create a RT Dashboard using CoPilot to auitomatically generate a report.
