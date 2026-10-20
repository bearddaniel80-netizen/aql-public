# Binary Operator

The binary operator allows you to limit query results to records that match specific conditions.

In AQL, the binary operator can be used in any or all of the following clauses: `WHERE`, `HAVING`, and `ORDER BY`. The binary operator may use [negation operators](negate.md) and optionally [logic operators](logic.md).
---

## SHOW
One can see the current binary operator list:
```bash
aql query "SHOW operators"
```
---

## DESCRIBE
One can see the data types in the binary operator list:
```bash
aql query "DESCRIBE operators"
```
---

## SELECT
One can query the current binary operator list:
```bash
aql query "SELECT * FROM operators"
```
---

## Common table expression (CTE)
One can query the current binary operator list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM operators ) SELECT * FROM generic_cte"
```
---

The binary operator will work on all sources; here we will show JSON source.

---
Binary Operator count: 13

## BETWEEN
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age BETWEEN 26 AND 46
```
---

## IN
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age IN [26, 46]
```
---

## ~=
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name ~= 'Jim'
```
---

## !=
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age != 26
```
---

## <=
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age <= 26
```
---

## >=
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age >= 26
```
---

## =
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name ~= 'Jim'
```
---

## <
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age <= 26
```
---

## >
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE age >= 26
```
---

## LIKE
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name LIKE 'Jim'
```
---

## CONTAINS
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name CONTAINS 'Jim'
```
---

## STARTSWITH
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name STARTSWITH 'Jim'
```
---

## ENDSWITH
### Basic syntax
```sql
SELECT name FROM json('data.json') WHERE name ENDSWITH 'Jim'
```
---


Binary Operator count: 13
