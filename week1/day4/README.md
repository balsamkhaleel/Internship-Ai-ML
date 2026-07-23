\# Day 4 — Pandas: Tabular Data



\## Summary

Worked with a real dataset in Pandas, covering the full workflow from loading and inspecting data to cleaning it and summarizing it with groupby aggregation.



\## Key Concepts

\- Series vs. DataFrame

\- Loading and inspecting data: read\_csv, head, info, describe

\- Selecting and filtering: boolean filtering, .loc/.iloc

\- Cleaning: missing values, duplicates, type conversion

\- Grouping and aggregation: groupby, agg (split-apply-combine)



\## Tasks

\- Loaded a CSV dataset into a DataFrame and inspected its shape, columns, and dtypes.

\- Counted missing values per column and handled them with fillna and dropna, with a documented justification.

\- Selected columns and filtered rows by condition using boolean filtering and .loc/.iloc.

\- Removed duplicate rows using drop\_duplicates.

\- Used groupby and agg to compute aggregate statistics per category and interpreted the results in a Markdown cell.



\## Key Takeaway

Cleaning and structuring real-world data is often the largest part of any ML project — everything downstream depends on getting this step right.



\## Files

\- `day4.ipynb` — data loading, cleaning, filtering, and groupby aggregation exercises.

