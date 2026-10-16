# GroupBy clause

The group by clause allows you query with aggregate functions.

In AQL, the group by clause can be used with the following clauses: `HAVING` or `ORDER BY`. The group by clause combins with [binary operators](binaryop.md) and optionally [logic operators](logic.md).
The group by clause will work on all sources; here we will show JSON source.

---

## Basic Syntax

```sql 
SELECT * FROM json('data.json') GROUP BY age HAVING AVG(age) != 26
```
Or an individual field:

```sql
SELECT name FROM json('data.json') GROUP BY age
```

Only records matching the condition are returned.

## Common Table Expressions

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') GROUP BY age ) SELECT * FROM generic_cte
```