# Negation Operatortor

The negation operator allows you to reverse results to records that match.

In AQL, the negation operator can be used in any or all of the following clauses: `WHERE`, `HAVING`, and `ORDER BY`. The negation operator ALWYS combins with [binary operators](binaryop.md) and optionally [logic operators](logic.md).
The negation operator will work on all sources; here we will show JSON source.

---

## Basic Syntax

```sql 
<neg:star>
```

Or an individual field:

```sql
<neg:single>
```

Some operators have unique orders:

## BETWEEN

```sql

```

## IN

```sql

```

Only records matching the condition are returned.

## HAVING

```sql

```

## ORDER BY

```sql

```

## Common Table Expressions

```sql
WITH generic_cte AS ( SELECT name FROM json('data.json') WHERE NOT age BETWEEN 26 AND 46 ) SELECT * FROM generic_cte
```