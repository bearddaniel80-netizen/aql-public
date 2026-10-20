# JSON

The `json()` source allows AQL to query JSON files using standard SQL-inspired syntax.

JSON files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Commandline execution

```bash
aql query "SELECT * FROM json('data.json')"
```

## Query Patterns

Select all columns:

```sql
SELECT * FROM json('data.json')
```

Select specific columns:

```sql
SELECT name FROM json('data.json')
```

## Common Table Expressions:

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') ) SELECT * FROM generic_cte
```

---