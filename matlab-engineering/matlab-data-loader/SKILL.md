---
name: matlab-data-loader
description: Use when loading, validating, and normalizing data in MATLAB from MAT, CSV, TXT, XLSX, JSON, or mixed tabular files for downstream analysis or modeling.
---

# MATLAB Data Loader

## Purpose

Load external data into MATLAB with stable typing, shape checks, and reproducible preprocessing.

## When to use

- MAT file loading
- CSV, TXT, and spreadsheet import
- JSON and structured text ingestion
- Converting tables to arrays or timetables
- Cleaning missing values and metadata

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) when exporting cleaned data.

## Workflow

1. Inspect file type, schema, delimiters, headers, and time fields.
2. Choose the narrowest correct loader: `load`, `readtable`, `readmatrix`, `readcell`, or `jsondecode`.
3. Validate shape, missing values, units, and variable names.
4. Convert to `table`, `timetable`, or numeric arrays explicitly.
5. Save a normalized dataset if the workflow will be reused.

## Always

- Preserve original column names unless there is a strong reason to normalize them.
- Handle missing values explicitly.
- Keep timestamps and time zones clear.
- Avoid silent type coercion.
- Print or return a compact schema summary after loading.

## Example code

```matlab
T = readtable('data.csv');
summary(T)
assert(~isempty(T), 'Loaded table is empty');
```
