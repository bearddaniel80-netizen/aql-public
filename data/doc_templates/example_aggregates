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
Aggregate count: <aggregate:count>

<aggregate:list>

Aggregate count: <aggregate:count>
