# Datasets

All datasets in this folder are **synthetic** (randomly generated) and free to use for any purpose.

## Included files

| File | Rows | Description |
|------|------|-------------|
| `employees.csv` | 50 | Synthetic employee records: id, name, department, salary, hire date, city, age |
| `sales.csv` | 500 | Synthetic retail transactions: transaction id, date, product, category, quantity, unit price, region, customer id |

## Generated locally (not in git)

| File | Rows | How to create |
|------|------|---------------|
| `sales_large.csv` | 100,000 | Run `python scripts/generate_large_data.py` from the repo root |

The large dataset uses the same schema as `sales.csv` and is used in the big data notebooks to demonstrate tools like PySpark, Dask, and DuckDB.
