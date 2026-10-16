# XML

The `xml()` source allows AQL to query XML files using standard SQL-inspired syntax.

XML files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

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
SELECT name FROM xml('data.xml')
```

## Common Table Expressions:

```sql
<cte:single>
```

---