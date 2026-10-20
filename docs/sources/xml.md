# XML

The `xml()` source allows AQL to query XML files using standard SQL-inspired syntax.

XML files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Commandline execution

```bash
aql query "SELECT * FROM xml('data.xml')"
```

## Query Patterns

Select all columns:

```sql
SELECT * FROM xml('data.xml')
```

Select specific columns:

```sql
SELECT name FROM xml('data.xml')
```

## Common Table Expressions:

```sql
WITH generic_cte AS ( SELECT name FROM xml('data.xml') ) SELECT * FROM generic_cte
```

---