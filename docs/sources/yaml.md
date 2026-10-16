# YAML

The `yaml()` source allows AQL to query YAML files using standard SQL-inspired syntax.

YAML files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

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
SELECT name FROM yaml('data.yml')
```

## Common Table Expressions:

```sql
<cte:single>
```

---