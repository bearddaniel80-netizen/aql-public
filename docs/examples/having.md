# Having clause

The having clause allows you filter aggregated results. As the results are always [aggregates](aggregates.md) [group by clause](groupby.md) must ALWAYS be present.

In AQL, the having clause can be used with the following clauses: `GROUP BY` or `ORDER BY`. The having clause combins with [binary operators](binaryop.md) and optionally [logic operators](logic.md).
The having clause will work on all sources and field aliases; here we will show JSON source.

---

## Basic Syntax

```sql 
SELECT * FROM json('data.json') GROUP BY age HAVING AVG(age) != 26
```
Or an individual field:

```sql
SELECT name FROM json('data.json') GROUP BY age HAVING AVG(age) != 26
```

Only records matching the condition are returned.

## Common Table Expressions

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') GROUP BY age HAVING AVG(age) != 26 ) SELECT * FROM generic_cte
```