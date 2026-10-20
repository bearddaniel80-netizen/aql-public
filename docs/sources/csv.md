# CSV

The `csv()` source allows AQL to query CSV files using standard SQL-inspired syntax.

CSV files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Commandline execution

```bash
aql query "SELECT * FROM csv('data.csv')"
```

## Query Patterns

Select all columns:

```sql
SELECT * FROM csv('data.csv')
```

Select specific columns:

```sql
SELECT name FROM csv('data.csv')
```

## Common Table Expressions:

```sql
WITH generic_cte AS ( SELECT name FROM csv('data.csv') ) SELECT * FROM generic_cte
```

---