This document walks the user through delivering this Fabric and PBI CoPilot demo. Prompts to put into the CoPilot pane `are put in these code blocks` and instructions are written out. What you need to do to prep for each section is also listed.

# Stock Market (KQL Queryset, Real Time Dashboard)

---

## Introduction

This demo showcases how to use Copilot within Microsoft Fabric to generate KQL queries and create real-time dashboards using natural language. The scenario uses high-volume, high-velocity fake stock market data created by the event stream. The walkthrough covers exploring data, generating queries, building dashboards, and troubleshooting—all with Copilot’s AI-powered assistance. 

---

## Fabric Resources

To follow along, browse to the **KQL & RTI CoPilot Capabilities Demo** folder in your Fabric Workspace. You’ll find:

- **KQL & RTI Demo Notebook (complete):**  
  Contains all prompts and executed results for the demo.

- **KQL & RTI Demo Notebook (steps):**  
  An empty notebook listing the prompts, ready for you to execute step-by-step.

---

## Disclaimer

Copilot generates queries and dashboards from scratch each time you use it, so results may vary. Outputs can be code, text explanations, or a mix of both. The experience may differ depending on your prompts, the data schema, and Copilot’s interpretation. Always review the generated queries and dashboards for accuracy and relevance to your scenario. 

---

## Tips

- **Variable Naming:**  
  Variable and table names may differ from what you expect. Double-check that the generated queries reference the correct data sources.

- **Error Handling:**  
  If you encounter errors, use Copilot’s “fix this error” feature or manually adjust the code. Having a completed notebook or dashboard as a backup can be helpful during live demos.

- **Data Validation:**  
  Always check your results. For example, if a dashboard references “bikes data” when you uploaded stock market data, investigate and correct any mismatches.

- **Iterative Prompting:**  
  If Copilot’s initial output isn’t what you need, try rephrasing your prompt or providing more specific instructions.

- **Live Demo Preparation:**  
  Have a completed notebook or dashboard ready as a backup in case Copilot cannot generate the desired output during your presentation.

---

## Prep
This data uses the `StockMarket` fake streaming data from the Eventstream. Setup the eventstream to ingest this data stream into an Eventhouse.

## KQL Queryset
*  Natural Language to KQL Examples
    - `for each stock, get the average price over the past hour, round to two decimal places`
    - `sum of all stock sales for the past 30 minutes`
    - `calculate the increase for each stock over the past half hour`
    - `show in a tumbling window 1 minute long, for the past half hour, total sales for the HOOJ stock round to two decimal places`

## Real Time Dashboard
* Go to the `Real Time Hub` on the left hand navigation pane. Select the `StockMarket` streaming data and select the settings for it. Select the `Create Real-time Dashboard (Preview)` option. This create a RT Dashboard using CoPilot to auitomatically generate a report.
