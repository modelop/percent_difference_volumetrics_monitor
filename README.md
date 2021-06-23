# Even identifiers volumetrics model


This is an example model with a semi-custom volumetrics monitoring test. The model extends the volumetrics count comparison by calculating a percent difference between the counts of the two dataframes and adds that calculation as a new test in the model test results.

Two example input files are included:

- `df_baseline_scored.json` is copied from the [German credit model](https://github.com/merhi-odg/german_credit_python/tree/extended_schema).
- `df_sample_scored.json` is copied from the [German credit model](https://github.com/merhi-odg/german_credit_python/tree/extended_schema).

To test this monitor, follow these steps:

- Import this repo into MOC and create a snapshot. Attach a runtime to the snapshot that has the [monitoring package](https://github.com/modelop/moc_monitors) installed.
- Import the [German credit model](https://github.com/merhi-odg/german_credit_python/tree/extended_schema) (`extended_schema` branch) and create a snapshot.
- In the German credit snapshot, add this monitor. The association role `DATA_DRIFT_MODEL` should already be selected. For the baseline asset, add the `df_baseline_scored.json` asset in the German credit model, and for the sample data asset add the `df_sample_scored.json` asset that's already stored in the German credit model.
- Run the monitor either via a schedule or manual run, and the test result should be a "Count Percent Difference" table with an `percent_difference` column
