# Dataset and preprocessing
After deciding to explore the correlation between fast food consumption and obesity, our next step was to find datasets that could reveal correlations from two different perspectives. We initially looked for relevant datasets with sufficient data to support our analysis. This was challenging because many of the datasets we reviewed did not show the expected correlations. Eventually, we chose 8 diverse datasets. More information about the datasets and the chosen variables can be found below.

## Cleaning
Each dataset required some modifications, such as renaming columns or making structural changes.

To make the best use of the selected datasets, we began by thoroughly cleaning and preprocessing them. Our first step was to rename columns and ensure the state identifiers were consistent across all datasets; some used state codes while others used full state names, so we standardized them to match. Next, we decided which variables were relevant to our research and discarded the rest. At this point, all datasets were ready to be merged.

After merging, we reorganized some columns to improve the usability of the combined dataset. We then checked for missing values since some datasets included one or two states not present in others. These states were removed to maintain consistency, as we only wanted to include states present in all datasets. With cleaning and preprocessing complete, our dataset was ready for analysis.

## Variable descriptions

In terms of variable type and measurement scale, the variables in the final
dataset can be classified under several combinations:

- Continuous / Ratio variables: `Calories`, `Fat`, `Cholesterol`, `Sugar`, `Sodium`,
 `Average.Income`, `Obesity, total (% adults aged 20 and over)`, `Adult.Obesity*100`, 
 `Unemployment_rate_2015-2019`, `Percent of adults with a bachelor's degree or higher, 2015-19`, 
 `percent_democrat`, `All fast food restaurants`
- Discrete / Interval variables: `Year`
- Discrete / Nominal variables: `State`

Variables that are currently being used are: `Calories`, `Fat`, `Cholesterol`, `Sugar`, `Sodium`,
`Year`, `Obesity, total (% adults aged 20 and over)`, `State`, `Adult.Obesity*100`, `Average.Income`, 
`percent_democrat`, `All fast food restaurants`, `Unemployment_rate_2015-2019`, 
and `Percent of adults with a bachelor's degree or higher, 2015-19`.
