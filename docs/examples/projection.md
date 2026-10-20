# Projection

Projecting allows you to limit query results to records that match specific conditions.

In AQL, projecting is performed using the `SELECT` clause.
Projections will work on all sources; here we will show JSON source.

---

## Basic Syntax

```sql 
SELECT * FROM json('data.json')
```

Or an individual field:

```sql
SELECT name FROM json('data.json')
```

Only records matching the condition are returned.

## Common Table Expressions

```sql
<cte>
```