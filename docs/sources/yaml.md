# YAML

The `yaml()` source allows AQL to query YAML files using standard SQL-inspired syntax.

YAML files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Commandline execution

```bash
aql query "SELECT * FROM yaml('data.yml')"
```

## Query Patterns

Select all columns:

```sql
SELECT * FROM yaml('data.yml')
```

Select specific columns:

```sql
SELECT name FROM yaml('data.yml')
```

## Common Table Expressions:

```sql
WITH generic_cte AS ( SELECT name FROM yaml('data.yml') ) SELECT * FROM generic_cte
```

---