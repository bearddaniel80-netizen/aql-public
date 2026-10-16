# Common Table Expressions

The cte allows you to build temporary query which then be called as a table.

In AQL, the cte can be used with the following clauses: `SELECT`, `FROM`, `GROUP BY`, `WHERE`, `HAVING` or `ORDER BY`. The cte combins with [binary operators](binaryop.md) and optionally [logic operators](logic.md).
The cte will work on all sources; here we will show JSON source.

---

## Basic Syntax

```sql 
WITH generic_cte AS ( SELECT * FROM json('data.json') ) SELECT * FROM generic_cte
```
Or an individual field:

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') ) SELECT * FROM generic_cte
```

Only records matching the condition are returned.
