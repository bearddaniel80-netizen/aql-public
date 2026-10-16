# LOG

The `log()` source allows AQL to query LOG files using standard SQL-inspired syntax.

LOG files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Commandline execution

```bash
aql query ""
```

## Query Patterns

Select all columns:

```sql

```

Select specific columns:

```sql
SELECT name FROM log('data.log')
```

## Common Table Expressions:

```sql
<cte:single>
```

---