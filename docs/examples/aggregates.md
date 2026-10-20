# Aggregate Function

The aggregate allows you to limit query results to records that match specific conditions and mutate fields.

In AQL, the aggregate can be used in any or all of the following clauses: `SELECT`, `HAVING`, and `ORDER BY` but there must ALWAYS be `GROUP BY`. The aggregate may use [binary operator](binaryop.md), [negation operators](negate.md) and optionally [logic operators](logic.md).

---

## SHOW
One can see the current aggregate list:
```bash
aql query "SHOW aggregates"
```
---

## DESCRIBE
One can see the data types in the aggregate list:
```bash
aql query "DESCRIBE aggregates"
```
---

## SELECT
One can query the current aggregate list:
```bash
aql query "SELECT * FROM aggregates"
```
---

## Common table expression (CTE)
One can query the current aggregate list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM aggregates ) SELECT * FROM generic_cte"
```
---


The aggregate will work on all sources; here we will show JSON source.

---
Aggregate count: 5

## AVG
*Description:* Find average or mean of a collection.
*Takes:* int
*Returns:* float
### Basic syntax
```sql
SELECT name FROM json('data.json') GROUP BY age HAVING AVG(age) != 26
```
---

## COUNT
*Description:* Count elements in a collection.
*Takes:* int
*Returns:* int
### Basic syntax
```sql
SELECT name FROM json('data.json') GROUP BY age HAVING COUNT(age) <= 26
```
---

## MAX
*Description:* Find largest value in a collection.
*Takes:* int
*Returns:* int
### Basic syntax
```sql
SELECT name FROM json('data.json') GROUP BY age HAVING MAX(age) >= 26
```
---

## MIN
*Description:* Find smallest value in a collection.
*Takes:* int
*Returns:* int
### Basic syntax
```sql
SELECT name FROM json('data.json') GROUP BY age HAVING MIN(age) = 26
```
---

## SUM
*Description:* Add all values in a collection.
*Takes:* int
*Returns:* int
### Basic syntax
```sql
SELECT name FROM json('data.json') GROUP BY age HAVING SUM(age) < 26
```
---



Aggregate count: 5
