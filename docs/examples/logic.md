# Logic Operatortors

Logic operators allows you to limit query results to records that match combioned conditions.

In AQL, logic operators can be used in any or all of the following clauses: `WHERE`, `HAVING`, and `ORDER BY`. Also it can be combined with [negation operator](negsation.md), [binary operators](binaryop.md).
Logic Operators will work on all sources; here we will show JSON source.

---

## Basic Syntax

```sql 
<op:and:star>
```

```sql 
<op:or:star>
```

Or an individual field:

```sql
<op:and:single>
```

```sql
<op:or:single>
```

Only records matching the condition are returned.

## HAVING

```sql
SELECT name FROM json('data.json') GROUP BY age HAVING AVG(age) BETWEEN 26 AND 46
```

```sql
SELECT name FROM json('data.json') GROUP BY age HAVING AVG(age) > 26 OR AVG(age) BETWEEN 46 AND 26
```

## ORDER BY

```sql

```

```sql

```

## Common Table Expressions

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') WHERE age BETWEEN 26 AND 46 ) SELECT * FROM generic_cte
```

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') WHERE age IN [26, 46] OR name IN ['Jim', 'Bob'] ) SELECT * FROM generic_cte
```